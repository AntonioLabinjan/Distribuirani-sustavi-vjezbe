Project Service

Opis:
Mikroservis za CRUD operacije nad projektima studenata.

Funkcionalnosti:

Dodavanje, uređivanje i brisanje projekata

Povlačenje liste svih projekata

Zahtjevi:

Python 3.12+

Pip

SQLite3 (ugrađen u Python)

Instalacija i pokretanje:

Instaliraj dependencies:
pip install -r requirements.txt

Pokreni server lokalno:
uvicorn app:app --reload --host 127.0.0.1 --port 8000

Servis će biti dostupan na: http://127.0.0.1:8000

Endpoints:

GET /projects : Dohvati sve projekte

POST /projects : Dodaj novi projekt

POST /edit/{id} : Uredi postojeći projekt

DELETE /projects/{id} : Obriši projekt

Napomene:

Servis koristi SQLite bazu projects.db
