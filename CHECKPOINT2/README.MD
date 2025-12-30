CHECKPOINT2 - Distribuirani Sustavi (Lokalno Pokretanje)

Opis:
Ovo je mikroservisna aplikacija za upravljanje projektima studenata. 
Sastoji se od četiri mikroservisa:

1. Auth Service      - autentikacija korisnika (port 8002)
2. Project Service   - CRUD operacije nad projektima (port 8000)
3. Stats Service     - statistike o projektima i studentima (port 8001)
4. Frontend Service  - web sučelje (port 5000)

Svi servisi komuniciraju preko HTTP-a koristeći REST API. 
Frontend komunicira sa svim servisima, a Stats Service fetcha podatke iz Project Service.

Struktura:
- /auth-service
- /project-service
- /stats-service
- /frontend-service

Pokretanje servisa lokalno:

1. Otvori terminal u direktoriju svakog servisa i pokreni:
   uvicorn app:app --reload --host 0.0.0.0 --port <PORT>

   Primjeri:
   Auth Service:    uvicorn app:app --reload --host 0.0.0.0 --port 8002
   Project Service: uvicorn app:app --reload --host 0.0.0.0 --port 8000
   Stats Service:   uvicorn app:app --reload --host 0.0.0.0 --port 8001
   Frontend:        uvicorn app:app --reload --host 0.0.0.0 --port 5000

2. Otvori frontend u pregledniku:
   http://localhost:5000

Napomene:
- Frontend koristi JWT autentikaciju preko Auth Service
- Stats Service fetcha projekte iz Project Service kako bi prikazao statistike
- Svaki servis čita svoje okoline varijable iz .env fajla ako je potrebno
- Za debug: prati logove u terminalu gdje je servis pokrenut

PlantUML dijagram komunikacije se nalazi u datoteci arhitektura.svg

