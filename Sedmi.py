def filtriraj_parne(lista):
  nova_lista = []
  for broj in lista:
    if broj % 2 == 0:
      nova_lista.append(broj)
  return nova_lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(filtriraj_parne(lista))
     