lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]

def prvi_i_zadnji(lista):
    prvi = lista[0]
    zadnji = lista[-1]
    
    return(prvi, zadnji)

print(prvi_i_zadnji(lista))
    
def maks_i_min(lista):
    minimum = lista[0]
    maksimum = lista[0]

    for broj in lista[1:]:
        if broj < minimum:
            minimum = broj
        elif broj > maksimum:
            maksimum = broj

    return (maksimum, minimum)


print(maks_i_min(lista)) 

def presjek(skup1, skup2):
    rezultat = set()
    for element in skup1:
        if element in skup2:
            rezultat.add(element)
    return rezultat


skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}

print(presjek(skup_1, skup_2))  