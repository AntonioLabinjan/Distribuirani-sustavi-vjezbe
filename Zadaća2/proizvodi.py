skladiste = []

class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}, Cijena: {self.cijena}, Dostupna kolicina: {self.dostupna_kolicina}")

def dodaj_proizvod(proizvod):
    if isinstance(proizvod, Proizvod):
        skladiste.append(proizvod)

skladiste.append(Proizvod("Rakija", 30, 15))
skladiste.append(Proizvod("Sladoled", 2, 10))
