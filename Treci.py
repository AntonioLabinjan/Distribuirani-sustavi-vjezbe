import random

tajni_broj = random.randint(1, 100)
broj_pokusaja = 0
pogodak = False

while not pogodak:
    broj = int(input("Pogodi broj! "))
    broj_pokusaja += 1

    if broj == tajni_broj:
        print(f"Bravo, pogodio si nakon {broj_pokusaja} pokušaja!")
        pogodak = True
    elif broj > tajni_broj:
        print("Manji je od tog broja!")
    else:
        print("Veći je od tog broja!")

print("Kraj igre! Pokreni program ponovo ako želiš igrati opet!")