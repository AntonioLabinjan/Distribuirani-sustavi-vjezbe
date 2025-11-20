from flask import Flask, request, redirect, render_template_string
from data.storage import (
    init_db,
    get_all_projects,
    add_project,
    delete_project,
    get_project_by_id,
    edit_project
)

#html string jer mi se ni dalo delat templates folder :D
HTML_INDEX = """
<h1 style='font-family:Arial'>Evidencija studentskih projekata</h1>

<form method="POST" action="/add">
    <input name="student_name" placeholder="Ime studenta" required>
    <input name="project_title" placeholder="Naslov projekta" required>
    <input name="description" placeholder="Kratak opis" required>
    <button type="submit">Dodaj projekt</button>
</form>

<hr>

<h2>Popis projekata</h2>
<ul>
{% for p in projects %}
    <li>
        <b>{{p['project_title']}}</b> - {{p['student_name']}}<br>
        {{p['description']}}<br>

        <form method="POST" action="/delete/{{p['id']}}">
            <button>Obriši</button>
        </form>

        <form method="GET" action="/edit/{{p['id']}}">
            <button>Uredi</button>
        </form>

        <hr>
    </li>
{% endfor %}
</ul>
"""


HTML_EDIT = """
<h1>Uredi projekt</h1>

<form method="POST">
    <input name="student_name" value="{{p['student_name']}}" required>
    <input name="project_title" value="{{p['project_title']}}" required>
    <input name="description" value="{{p['description']}}" required>
    <button type="submit">Spremi</button>
</form>

<a href="/">Natrag</a>
"""


# init aplikacije i baze
def create_app():
    app = Flask(__name__)
    init_db()
    # ruta za dohvat svih podataka + dinamički rendering HTML-a i podataka
    @app.route("/")
    def index():
        projects = get_all_projects()
        return render_template_string(HTML_INDEX, projects=projects)
    # poziv funkcije add project pri svakom postu; podaci se dohvaćaju iz requesta (upisani u form)
    @app.route("/add", methods=["POST"])
    def add():
        add_project(
            student_name=request.form["student_name"],
            title=request.form["project_title"],
            description=request.form["description"],
        )
        return redirect("/")
        
    # birsanje po id-ju
    @app.route("/delete/<int:pid>", methods=["POST"])
    def delete(pid):
        delete_project(pid)
        return redirect("/")

    # eddit po id-ju; dinamički rendering edit forme
    @app.route("/edit/<int:pid>", methods=["GET", "POST"])
    def edit(pid):
        if request.method == "GET":
            p = get_project_by_id(pid)
            return render_template_string(HTML_EDIT, p=p)

        # POST za promjene
        edit_project(
            pid=pid,
            new_student_name=request.form["student_name"],
            new_name=request.form["project_title"],
            new_description=request.form["description"]
        )
        return redirect("/")

    return app
