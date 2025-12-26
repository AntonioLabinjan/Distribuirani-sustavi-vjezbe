from fastapi import FastAPI
import requests

PROJECT_SERVICE = "http://project-service:8000"

app = FastAPI()


@app.get("/stats/projects/count")
def count_projects():
    r = requests.get(f"{PROJECT_SERVICE}/projects")
    return {"count": len(r.json())}
