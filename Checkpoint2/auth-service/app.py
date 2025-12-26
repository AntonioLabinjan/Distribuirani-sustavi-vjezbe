from fastapi import FastAPI, Request, Form, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import requests

AUTH_API = "http://localhost:8002"
PROJECT_API = "http://localhost:8000"
STATS_API = "http://localhost:8001"

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# simple in-memory session store
session_tokens = {}

def get_current_user(request: Request):
    token = request.cookies.get("token")
    if not token or token not in session_tokens.values():
        return None
    return token

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login(response: Response, username: str = Form(...), password: str = Form(...)):
    r = requests.post(f"{AUTH_API}/login", data={"username": username, "password": password})
    if r.status_code != 200 or "access_token" not in r.json():
        return RedirectResponse("/login", status_code=303)
    token = r.json()["access_token"]
    session_tokens[username] = token
    response = RedirectResponse("/", status_code=303)
    response.set_cookie(key="token", value=token)
    return response

@app.get("/logout")
def logout(request: Request, response: Response):
    token = request.cookies.get("token")
    if token:
        user = next((u for u, t in session_tokens.items() if t == token), None)
        if user:
            session_tokens.pop(user)
    response = RedirectResponse("/login", status_code=303)
    response.delete_cookie("token")
    return response

@app.get("/", response_class=HTMLResponse)
@app.post("/", response_class=HTMLResponse)
async def index(request: Request,
                student_name: str = Form(None),
                project_title: str = Form(None),
                description: str = Form(None)):
    
    token = get_current_user(request)
    if not token:
        return RedirectResponse("/login", status_code=303)

    headers = {"Authorization": f"Bearer {token}"}

    # Dodavanje projekta
    if request.method == "POST" and student_name and project_title and description:
        requests.post(f"{PROJECT_API}/projects", json={
            "student_name": student_name,
            "project_title": project_title,
            "description": description
        }, headers=headers)
        return RedirectResponse("/", status_code=303)

    # Povuci projekte i statistike
    projects = requests.get(f"{PROJECT_API}/projects", headers=headers).json()
    total_count = requests.get(f"{STATS_API}/stats/projects/count", headers=headers).json()["count"]

    # Top studenti i broj projekata
    top_students = requests.get(f"{STATS_API}/stats/projects/top-students", headers=headers).json()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "projects": projects,
        "count": total_count,
        "top_students": top_students
    })

@app.post("/delete/{pid}")
async def delete(pid: int, request: Request):
    token = get_current_user(request)
    if not token:
        return RedirectResponse("/login", status_code=303)
    headers = {"Authorization": f"Bearer {token}"}
    requests.delete(f"{PROJECT_API}/projects/{pid}", headers=headers)
    return RedirectResponse("/", status_code=303)

@app.post("/edit/{pid}")
async def edit(pid: int, request: Request,
               student_name: str = Form(...),
               project_title: str = Form(...),
               description: str = Form(...)):
    token = get_current_user(request)
    if not token:
        return RedirectResponse("/login", status_code=303)
    headers = {"Authorization": f"Bearer {token}"}
    requests.post(f"{PROJECT_API}/edit/{pid}", data={
        "student_name": student_name,
        "project_title": project_title,
        "description": description
    }, headers=headers)
    return RedirectResponse("/", status_code=303)

@app.post("/signup")
async def signup(request: Request, username: str = Form(...), password: str = Form(...)):
    r = requests.post(f"{AUTH_API}/signup", data={"username": username, "password": password})
    if r.status_code != 200:
        return RedirectResponse("/login", status_code=303)
    # nakon signup-a automatski login
    login_resp = requests.post(f"{AUTH_API}/login", data={"username": username, "password": password})
    if login_resp.status_code != 200:
        return RedirectResponse("/login", status_code=303)
    token = login_resp.json()["access_token"]
    session_tokens[username] = token
    response = RedirectResponse("/", status_code=303)
    response.set_cookie(key="token", value=token)
    return response
