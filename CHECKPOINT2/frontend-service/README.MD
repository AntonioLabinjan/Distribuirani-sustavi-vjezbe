Frontend Service

Opis:
Web aplikacija za prikaz i upravljanje projektima studenata.

Funkcionalnosti:

Login / Signup

Dodavanje, uređivanje i brisanje projekata

Prikaz statistike projekata i top studenata

Komunikacija s mikroservisima (Auth, Project, Stats)

Zahtjevi:

Python 3.12+

Pip

FastAPI, Jinja2, Requests

Instalacija i pokretanje:

Instaliraj dependencies:
pip install -r requirements.txt

Postavi environment varijable (ako želiš mijenjati portove):
AUTH_API="http://127.0.0.1:8002
"
PROJECT_API="http://127.0.0.1:8000
"
STATS_API="http://127.0.0.1:8001
"

Pokreni server lokalno:
uvicorn app:app --reload --host 127.0.0.1 --port 5000

Otvori browser: http://127.0.0.1:5000

Napomene:

Frontend koristi cookie-based sessions za login

Za lokalni test nije potreban Docker
