from fastapi import FastAPI
import requests
from collections import Counter

PROJECT_SERVICE = "http://localhost:8000"
app = FastAPI()

@app.get("/stats/projects/count")
def count_projects():
    r = requests.get(f"{PROJECT_SERVICE}/projects")
    return {"count": len(r.json())}

@app.get("/stats/projects/top-students")
def top_students(limit: int = 5):
    r = requests.get(f"{PROJECT_SERVICE}/projects")
    students = [p["student_name"] for p in r.json()]
    most_common = Counter(students).most_common(limit)
    return [{"student_name": s, "projects": n} for s, n in most_common]

@app.get("/stats/projects/top-titles")
def top_titles(limit: int = 5):
    r = requests.get(f"{PROJECT_SERVICE}/projects")
    titles = [p["project_title"] for p in r.json()]
    most_common = Counter(titles).most_common(limit)
    return [{"title": t, "count": n} for t, n in most_common]

@app.get("/stats/projects/recent")
def recent_projects(limit: int = 5):
    r = requests.get(f"{PROJECT_SERVICE}/projects")
    projects = r.json()
    projects.sort(key=lambda x: x["id"], reverse=True)
    return projects[:limit]
