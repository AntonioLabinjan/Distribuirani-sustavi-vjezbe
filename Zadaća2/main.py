from proizvodi import Proizvod, skladiste, dodaj_proizvod
from narudzbe import napravi_narudzbu

print("si ziv??")

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Mis", "cijena": 100, "dostupna_kolicina": 100}
]

for p in proizvodi_za_dodavanje:
    dodaj_proizvod(Proizvod(p["naziv"], p["cijena"], p["dostupna_kolicina"]))

for p in skladiste:
    p.ispis()

lista_za_narudzbu = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1},
    {"naziv": "Rakija", "cijena": 30, "narucena_kolicina": 1}
]

narudzba = napravi_narudzbu(lista_za_narudzbu)
if narudzba:
    narudzba.ispis_narudzbe()
