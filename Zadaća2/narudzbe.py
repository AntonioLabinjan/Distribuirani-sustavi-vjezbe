from proizvodi import skladiste, Proizvod

narudzbe = []  

class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        proizvodi_str = ", ".join([f"{p['naziv']} x {p['narucena_kolicina']}" for p in self.naruceni_proizvodi])
        print(f"Naruceni proizvodi: {proizvodi_str}, Ukupna cijena: {self.ukupna_cijena} eur")

def napravi_narudzbu(lista_proizvoda):
    if not isinstance(lista_proizvoda, list) or not lista_proizvoda:
        print("Nisi nis narucia!")
        return None

    for p in lista_proizvoda:
        if not isinstance(p, dict):
            print("Moras prosljedit dictionaries")
            return None
        if not all(k in p for k in ["naziv", "cijena", "narucena_kolicina"]):
            print(f"Greska: dict {p} nima sve ključeve")
            return None
        pro_u_skladistu = next((s for s in skladiste if s.naziv == p["naziv"]), None)
        if not pro_u_skladistu or pro_u_skladistu.dostupna_kolicina < p["narucena_kolicina"]:
            print(f"Proizvoda {p['naziv']} ni!")
            return None

    ukupna_cijena = sum(p["cijena"] * p["narucena_kolicina"] for p in lista_proizvoda)

    nova_narudzba = Narudzba(lista_proizvoda, ukupna_cijena)
    narudzbe.append(nova_narudzba)
    return nova_narudzba
