# Aplikacija za evidenciju studentskih projekata

Kratki, jasni opis aplikacije (1–2 rečenice).
Aplikacija služi za jednostavnu evidenciju studentskih projekata i njihovo uređivanje. 


---

## 1. Svrha aplikacije

Tema projektnog zadatka odnosi se na evidenciju studentskih projekata te bilježi informacije o imenu studenta, nazivu projekta i opisu projekta.

Krajnji korisnici aplikacije su studenti koji mogu evidentirati svoje projekte i profesori koji mogu pregledavati te iste projekte.

Svaki se projekt bilježi u foramtu:

- ime studenta
- naziv projekta
- opis projekta

Ključne funkcionalnosti aplikacije su CRUD operacije na projektima i automatsko brojanje svih dodanih projekata.
---

## 🧱 2. Arhitektura i način implementacije

Ovdje ukratko objasni svoju implementaciju:

- koristiš li CLI ili GUI (npr. Typer, Tkinter, Streamlit…)
- koja je osnovna struktura aplikacije (paketi / moduli),
- koje su glavne komponente (UI, core logika, data layer),
- način pohrane podataka (npr. JSON / SQLite / in-memory),
- zašto aplikacija ispunjava uvjet *self-contained*.

Možeš uključiti strukturu direktorija, npr.:

```

my_app/
├── main.py
├── requirements.txt
├── README.md
├── myapp/
│   ├── ui/
│   ├── core/
│   ├── data/
│   └── utils/

````

---

## 🛠️ 3. Instalacija i pokretanje

Upute moraju biti 100% reproducibilne.

### 3.1. Kloniranje repozitorija

```bash
git clone <URL_do_repa>
cd <folder>
````

### 3.2. Kreiranje i aktivacija virtualnog okruženja

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3.3. Instalacija ovisnosti

```bash
pip install -r requirements.txt
```

### 3.4. Pokretanje aplikacije

```bash
python main.py
```

> Aplikacija se mora moći pokrenuti **jednom naredbom**.

---

## 📂 4. Korištenje aplikacije

Ovdje napiši:

* kako korisnik upravlja aplikacijom,
* kratke primjere (CLI naredbi ili GUI screenshot opis),
* opis osnovnih funkcionalnosti.

---

## 🗄️ 5. Tehnologije i ovisnosti

Nabroji ključne stvari koje koristiš, npr.:

* Python 3.12
* Typer / Tkinter / Streamlit / Flask …
* SQLite / JSON / CSV
* bilo koji dodatni pip modul (ako postoji)

---

## 📦 6. Način pohrane podataka

Objasni:

* što pohranjuješ,
* gdje se podaci spremaju (lokalna datoteka ili baza),
* format (JSON / CSV / SQLite),
* gdje se fizički nalazi datoteka.

---

## 🧪 7. Testiranje (opcionalno)

Ako imaš testove:

* kako se pokreću,
* kratak opis što pokrivaju.

---

## 🧊 8. Bundled verzija aplikacije (opcionalni dodatni bodovi)

Ako radiš PyInstaller / zipapp paket:

* kratke upute kako ga pokrenuti,
* gdje se nalazi izlazna datoteka.

---

## 👤 Autor

Ime i prezime
Kolegij: Raspodijeljeni sustavi
Godina: 2025.

---

```

---

Ako želiš, napravim ti i:

🔹 *puni README* nakon što završiš app  
🔹 predložak za strukturu projekta  
🔹 ideju za temu zadatka ako još nisi 100% siguran  

Samo reci i gasimo!🔥
```
