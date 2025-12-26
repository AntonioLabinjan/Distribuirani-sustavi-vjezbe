from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

DB = "projects.db"

app = FastAPI()


def get_conn():
    return sqlite3.connect(DB, check_same_thread=False)


@app.on_event("startup")
def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT,
        project_title TEXT,
        description TEXT
    )
    """)
    conn.commit()
    conn.close()


class ProjectIn(BaseModel):
    student_name: str
    project_title: str
    description: str


@app.get("/projects")
def get_projects():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM projects")
    rows = c.fetchall()
    conn.close()
    return [
        {
            "id": r[0],
            "student_name": r[1],
            "project_title": r[2],
            "description": r[3],
        }
        for r in rows
    ]


@app.post("/projects")
def add_project(p: ProjectIn):
    conn = get_conn()
    c = conn.cursor()
    c.execute(
        "INSERT INTO projects (student_name, project_title, description) VALUES (?, ?, ?)",
        (p.student_name, p.project_title, p.description),
    )
    conn.commit()
    conn.close()
    return {"status": "ok"}


@app.delete("/projects/{pid}")
def delete_project(pid: int):
    conn = get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM projects WHERE id = ?", (pid,))
    conn.commit()
    conn.close()
    return {"status": "deleted"}
