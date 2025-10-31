def filtriraj_duple(lista):
  nova_lista = []
  for broj in lista:
    if broj not in nova_lista:
      nova_lista.append(broj)
  return nova_lista

lista = [1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 10, 22, 22, 23, 45]

print(filtriraj_duple(lista))