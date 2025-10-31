suma = 0
for i in range(2, 101, 2):
    suma += i
print("Suma parnih brojeva od 1 do 100 je:", suma)

suma = 0
i = 2
while i <= 100:
    suma += i
    i += 2
print("Suma parnih brojeva od 1 do 100 je:", suma)

neparni = []
for i in range(1, 20, 2): 
    neparni.append(i)
neparni.reverse()
print("Prvih 10 neparnih brojeva u obrnutom redoslijedu:", neparni)

neparni = []
i = 1
brojac = 0
while brojac < 10:
    neparni.append(i)
    i += 2
    brojac += 1
neparni.reverse()
print("Prvih 10 neparnih brojeva u obrnutom redoslijedu:", neparni)
