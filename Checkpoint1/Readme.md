# Aplikacija za evidenciju studentskih projekata

Aplikacija služi za jednostavnu evidenciju studentskih projekata i njihovo uređivanje. 


---

## 1. Svrha aplikacije

Tema projektnog zadatka odnosi se na evidenciju studentskih projekata te bilježi informacije o imenu studenta, nazivu projekta i opisu projekta.

Krajnji korisnici aplikacije su studenti koji mogu evidentirati svoje projekte i profesori koji mogu pregledavati te iste projekte.

Svaki se projekt bilježi u foramtu:

- ime studenta
- naziv projekta
- opis projekta

#### Ključne funkcionalnosti aplikacije su CRUD operacije na projektima i automatsko brojanje svih dodanih projekata.
---

## 2. Arhitektura i način implementacije

Aplikacija ima jednostavan HTML GUI implementiran kroz Flask, najjednostavniji Pythonov web-framework.
Jedini pip paket koji je potrebno instalirati za uporabu ove aplikacije je sam Flask zato jer su unutar njega zapakirane i backend i frontend funkcionalnosti, dok sqlite3 (korištena baza) dolazi automatski s Pythonom.
Aplikacija je građena modularno te se sastoji od 3 modula:

main.py
data/
  storage.py
ui/
  web.py

Aplikacija je self-contained jer ne ovisi o eksternim apijima/modulima nego se svi potrebni dijelovi nalaze unutar istog repoa.
Konkretni dijelovi ove aplikacije su:
- main.py => centralna datoteka koja služi za pokretanje servera
- storage.py => datoteka koja omogućava konekciju na bazu i definira osnovne operacije (CRUD + brojanje projekata) pomoću Python funkcija
- web.py => datoteka koja kreira frontend, definira app rute i omogućava interakciju s bazom pomoću funkcija definiranih unutar storage.py

Podaci se pohranjuju u jednostavnu sqlite bazu podataka s 1 tablicom:

CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT NOT NULL,
        project_title TEXT NOT NULL
    )

Tablica definira projekt. Svaki projekt se sastoji od auto-incremented id-ja, imena studenta i naslova projekta.
Svaki atribut je obavezan. Auto-generirani id je tipa integer, dok su student_name i project_title tipa text.
Sqlite je built-in Python paket koji nije potrebno dodatno instalirati.

GUI aplikacije definiran je kroz built-in Flask funkciju render_template_string koji omogućava pisanje frontenda na backendu u obliku stringa.
Zatim ta funkcija parsira string i kreira web stranice prema danom html kodu.


Također, aplikacija je zapakirana u .exe što omogućava njeno pokretanje i bez da korisnik ima Python ili bilo koji njegov dependency na računalu.

Struktura projekta:
```

distsys_checkpoint/
├── build
|   ├── main
|      ├── velika količina fajlova koju NE DIRAMO
|── data
|    ├── storage.py
|── dist
|    |── main.exe
|    |── projects.db (baza za exe)
├── requirements.txt
├── README.md
├── main.py
├── projects.db (baza kad delamo lokalno)
├── ui
|    ├── web.py
|── venv
|    ├── velika količina fajlova koju NE DIRAMO
````

---

## 3. Instalacija i pokretanje

### 3.1. Kloniranje repozitorija

```bash


C:\Users\Korisnik\Desktop>git clone https://github.com/AntonioLabinjan/Distribuirani-sustavi-vjezbe
Cloning into 'Distribuirani-sustavi-vjezbe'...
remote: Enumerating objects: 108, done.
remote: Counting objects: 100% (108/108), done.
remote: Compressing objects: 100% (96/96), done.
remote: Total 108 (delta 31), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (108/108), 55.38 KiB | 391.00 KiB/s, done.
Resolving deltas: 100% (31/31), done.

cd distribuirani-sustavi-vjezbe
cd checkpoint1
````

### 3.2. Kreiranje i aktivacija virtualnog okruženja

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```


### 3.3. Instalacija ovisnosti

```bash
pip install -r requirements.txt
```

### 3.4. Pokretanje aplikacije

```bash
python main.py
```

> Aplikacija se pokreće nakon ove naredbe
(venv) C:\Users\Korisnik\Desktop\Distribuirani-sustavi-vjezbe\Checkpoint1>python main.py
 * Serving Flask app 'ui.web'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
---

##  4. Korištenje aplikacije

Korisnik upravlja aplikacijom tako da u polja za input unosi podatke, dodaje projekt klikom na tipku dodaj projekt.
Zatim može editirati ili brisati projekt pritiskom na odgovarajuće tipke.

Funkcionalnosti koje korisnik može upotrebljavati su:

- CRUD nad projektima
- pregled broja projekata
---

## 5. Tehnologije i ovisnosti

* Python
* Flask
* Sqlite3
* Pyinstaller


## 6. Bundled verzija aplikacije

Bundled verzija aplikacije kreirane je kroz pyinstaller (pythonov py2exe konverter).
Executable aplikacije i baza nalaze se unutar dist foldera.
Exe se pokreće klikom na datoteku.

Otvara se terminal u kojem se nakon par sekundi pokreće aplikacija na identičan način kao da je korisnik instalirao sve dependecies i upisao python main.py te se aplikaciji ponovno pristupa klikom na link. (localhost:5000)


## Autor

- Antonio Labinjan
- Kolegij: Distribuirani sustavi
- Ak. godina: 2025/26

---

