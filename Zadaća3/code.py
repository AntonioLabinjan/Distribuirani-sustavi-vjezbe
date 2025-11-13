#Zadaci
'''
import asyncio

async def dohvati_podatke():
    await asyncio.sleep(3)
    
    podaci = [i for i in range(1, 11)]
    
    print("Podaci dohvaceni.")
    return podaci

async def main():
    rezultat = await dohvati_podatke()
    print("Rezultat:", rezultat)

asyncio.run(main())
'''

'''
import asyncio

async def dohvati_pacijente():
    await asyncio.sleep(3) 
    pacijenti = [
        {"ime": "Ivan", "dob": 34, "dijagnoza": "Lud"},
        {"ime": "Ana", "dob": 29, "dijagnoza": "Munjena"},
        {"ime": "Marko", "dob": 42, "dijagnoza": "Zgoren"},
    ]
    print("Pacijenti dohvaceni.")
    return pacijenti

async def dohvati_terapije():
    await asyncio.sleep(5)  
    terapije = [
        {"ime": "Ivan", "terapija": "Elektrošokovi"},
        {"ime": "Ana", "terapija": "Meditacija"},
        {"ime": "Marko", "terapija": "Hipnoza"},
    ]
    print("Terapije dohvacene.")
    return terapije

async def main():
    pacijenti, terapije = await asyncio.gather(
        dohvati_pacijente(),
        dohvati_terapije()
    )
    
    print("Rezultati:")
    print("Pacijenti:", pacijenti)
    print("Terapije:", terapije)

asyncio.run(main())
'''
'''
import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autorizacija(korisnik_iz_baze, lozinka_unesena):
    await asyncio.sleep(2)  
    for zapis in baza_lozinka:
        if zapis['korisnicko_ime'] == korisnik_iz_baze['korisnicko_ime']:
            if zapis['lozinka'] == lozinka_unesena:
                return f"Korisnik {korisnik_iz_baze['korisnicko_ime']}: Autorizacija uspjesna."
            else:
                return f"Korisnik {korisnik_iz_baze['korisnicko_ime']}: Autorizacija neuspjesna."
    return f"Korisnik {korisnik_iz_baze['korisnicko_ime']}: Lozinka nije pronadena u bazi."

async def autentifikacija(korisnik):
    await asyncio.sleep(3)  
    for zapis in baza_korisnika:
        if zapis['korisnicko_ime'] == korisnik['korisnicko_ime'] and zapis['email'] == korisnik['email']:
            return await autorizacija(zapis, korisnik['lozinka'])
    return f"Korisnik {korisnik['korisnicko_ime']} nije pronaden."

async def main():
    test_korisnik = {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com', 'lozinka': 'lozinka123'}
    rezultat = await autentifikacija(test_korisnik)
    print(rezultat)
    
    test_korisnik2 = {'korisnicko_ime': 'MarioBattifiaca', 'email': 'battifiaca@gmail.com', 'lozinka': '123'}
    rezultat2 = await autentifikacija(test_korisnik2)
    print(rezultat2)

asyncio.run(main())
'''
'''
import asyncio
import random

async def provjeri_parnost(broj):
    await asyncio.sleep(2) 
    if broj % 2 == 0:
        return f"Broj {broj} je paran."
    else:
        return f"Broj {broj} je neparan."

async def main():
    lista_brojeva = [random.randint(1, 100) for _ in range(10)]
    print("Random brojevi:", lista_brojeva)
    
    zadaci = [asyncio.create_task(provjeri_parnost(broj)) for broj in lista_brojeva]
    
    rezultati = await asyncio.gather(*zadaci)
    
    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())
'''

import asyncio

async def secure_data(podaci):
    await asyncio.sleep(3)

    return {
        'prezime': podaci['prezime'],
        'broj_kartice': hash(str(podaci['broj_kartice'])),
        'CVV': hash(str(podaci['CVV']))
    }

async def main():
    lista_podataka = [
        {'prezime': 'Horvat', 'broj_kartice': '4539 1488 0343 6467', 'CVV': '123'},
        {'prezime': 'Kovac', 'broj_kartice': '5500 0000 0000 0004', 'CVV': '987'},
        {'prezime': 'Babic', 'broj_kartice': '3400 0000 0000 009', 'CVV': '456'}
    ]
    
    zadaci = [asyncio.create_task(secure_data(p)) for p in lista_podataka]
    
    rezultati = await asyncio.gather(*zadaci)
    
    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())
