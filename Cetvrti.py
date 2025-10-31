zbroj = 0

while True:
    broj = int(input("Unesi cijeli broj (0 za kraj): "))
    if broj == 0:
        break
    zbroj += broj

print("Zbroj svih unesenih brojeva je:", zbroj)
