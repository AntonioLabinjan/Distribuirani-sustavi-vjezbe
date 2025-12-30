from fastapi import FastAPI, Request
import requests
from collections import Counter

PROJECT_SERVICE = "http://127.0.0.1:8000"
app = FastAPI()

def get_projects(auth):
    r = requests.get(
        f"{PROJECT_SERVICE}/projects",
        headers={"Authorization": auth}
    )
    r.raise_for_status()
    return r.json()

@app.get("/stats/projects/count")
def count_projects(request: Request):
    projects = get_projects(request.headers.get("Authorization"))
    return {"count": len(projects)}

@app.get("/stats/projects/top-students")
def top_students(request: Request, limit: int = 5):
    projects = get_projects(request.headers.get("Authorization"))
    students = [p["student_name"] for p in projects]
    most_common = Counter(students).most_common(limit)
    return [{"student_name": s, "projects": n} for s, n in most_common]

@app.get("/stats/projects/top-titles")
def top_titles(request: Request, limit: int = 5):
    projects = get_projects(request.headers.get("Authorization"))
    titles = [p["project_title"] for p in projects]
    most_common = Counter(titles).most_common(limit)
    return [{"title": t, "count": n} for t, n in most_common]

@app.get("/stats/projects/recent")
def recent_projects(request: Request, limit: int = 5):
    projects = get_projects(request.headers.get("Authorization"))
    projects.sort(key=lambda x: x["id"], reverse=True)
    return projects[:limit]
