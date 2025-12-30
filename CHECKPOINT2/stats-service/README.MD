Stats Service

Opis:
Mikroservis za statistiku projekata i studenata.

Funkcionalnosti:

Broj svih projekata

Top studenti po broju projekata

Zahtjevi:

Python 3.12+

Pip

Requests (za pozive prema project servisu)

Instalacija i pokretanje:

Instaliraj dependencies:
pip install -r requirements.txt

Pokreni server lokalno:
uvicorn app:app --reload --host 127.0.0.1 --port 8001

Servis će biti dostupan na: http://127.0.0.1:8001

Endpoints:

GET /stats/projects/count : Broj svih projekata

GET /stats/projects/top-students : Top studenti po broju projekata

Napomene:

Servis povlači podatke iz Project Service
