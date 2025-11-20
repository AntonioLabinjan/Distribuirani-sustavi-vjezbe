# crud nad bazon

import sqlite3
import os

DB_PATH = "projects.db"

'''
takivamo se na bazu od gori
'''
def get_conn():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

'''
konekcija => veza na bazu
cursor => kursor koji čita podatke red po red i omogućava da delamo upite
execute kreira tabelu za projekte
'''
def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT NOT NULL,
        project_title TEXT NOT NULL,
    )
    """)
    conn.commit()
    conn.close()

'''
funkcija prima ime, naslov i opis i to inserta u tablicu => POST
'''

def add_project(student_name, title, description):
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
    INSERT INTO projects (student_name, project_title, description)
    VALUES (?, ?, ?)
    """, (student_name, title, description))
    conn.commit()
    conn.close()


'''
dohvat svih podataka pomoću queryja
tornivamo na način da se iz svakega retka upita dohvaćaju pojedini stupci i vraćaju ko objekt
'''
def get_all_projects():
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
            "description": r[3]
        }
        for r in rows
    ]

'''
prosljedimo id
spojimo se na bazu
napravimo delete query
'''
def delete_project(pid):
    conn = get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM projects WHERE id = ?", (pid,))
    conn.commit()
    conn.close()

def get_project_by_id(pid):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM projects WHERE id = ?", (pid,))
    row = c.fetchone()
    conn.close()
    return row

def edit_project(pid, new_student_name, new_name, new_description):
    conn = get_conn()
    c = conn.cursor()
    c.execute(
        """
        UPDATE projects
        SET student_name = ?, project_title = ?, description = ?
        WHERE id = ?
        """,
        (new_student_name, new_name, new_description, pid)
    )
    conn.commit()
    conn.close()
