from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import requests

PROJECT_API = "http://project-service:8000"
STATS_API = "http://stats-service:8001"

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # koristi folder templates

@app.get("/", response_class=HTMLResponse)
@app.post("/", response_class=HTMLResponse)
async def index(request: Request,
                student_name: str = Form(None),
                project_title: str = Form(None),
                description: str = Form(None)):
    if request.method == "POST" and student_name and project_title and description:
        # dodavanje novog projekta
        requests.post(f"{PROJECT_API}/projects", json={
            "student_name": student_name,
            "project_title": project_title,
            "description": description
        })
        return RedirectResponse("/", status_code=303)

    # GET: dohvati projekte i broj
    projects = requests.get(f"{PROJECT_API}/projects").json()
    count = requests.get(f"{STATS_API}/stats/projects/count").json()["count"]

    # render iz foldera templates
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "projects": projects, "count": count}
    )

@app.post("/delete/{pid}")
async def delete(pid: int):
    requests.delete(f"{PROJECT_API}/projects/{pid}")
    return RedirectResponse("/", status_code=303)
