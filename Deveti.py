def brojanje_riječi(tekst):
    rijeci = tekst.split()
    brojac = {}

    for rijec in rijeci:
        if rijec in brojac:
            brojac[rijec] += 1
        else:
            brojac[rijec] = 1

    return brojac


tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(brojanje_riječi(tekst))