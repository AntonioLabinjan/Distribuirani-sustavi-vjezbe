Auth Service

Opis:
Mikroservis za autentikaciju korisnika (signup/login) koristeći FastAPI.

Funkcionalnosti:

Registracija korisnika (/signup)

Login korisnika (/login)

Generiranje i provjera JWT tokena

Zahtjevi:

Python 3.12+

Pip

Instalacija i pokretanje:

Instaliraj dependencies:
pip install -r requirements.txt

Pokreni server lokalno:
uvicorn app:app --reload --host 127.0.0.1 --port 8002

Servis će biti dostupan na: http://127.0.0.1:8002

Endpoints:

POST /signup : Registracija korisnika

POST /login : Login korisnika

Napomene:

JWT token se vraća prilikom login-a i koristi se za autorizaciju drugih servisa
