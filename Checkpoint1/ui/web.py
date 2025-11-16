from flask import Flask, request, redirect, render_template_string
from data.storage import init_db, get_all_projects, add_project, delete_project

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
        <b>{{p['project_title']}}</b> — {{p['student_name']}}<br>
        {{p['description']}}<br>

        <form method="POST" action="/delete/{{p['id']}}">
            <button>Obriši</button>
        </form>
        <hr>
    </li>
{% endfor %}
</ul>
"""

# init aplikacije i baze
def create_app():
    app = Flask(__name__)
    init_db()

    # /ruta za dogvat svih projekata pomoću funckije get_all_projects importane iz storage
    @app.route("/")
    def index():
        projects = get_all_projects()
        # kreiramo html page od onega stringa gore i dinamički dohvaćamo projekte iz baze
        return render_template_string(HTML_INDEX, projects=projects)

    # obična glupa post ruta; prima 3 parametra iz request forma, to prosljeđuje u add_project funkciju i šalje na server
    @app.route("/add", methods=["POST"])
    def add():
        add_project(
            student_name=request.form["student_name"],
            title=request.form["project_title"],
            description=request.form["description"],
        )
        return redirect("/")

    # dohvat po id-ju i prosljeđivanje istega u delete_project funkciju
    @app.route("/delete/<int:pid>", methods=["POST"])
    def delete(pid):
        delete_project(pid)
        return redirect("/")

    return app
