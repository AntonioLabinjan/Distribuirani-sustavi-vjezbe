godina = int(input("Unesi godinu: "))
if godina % 4 == 0 or godina % 100 == 0 or godina % 400 == 0:
  print("Godina je prijestupna")
else:
  print("Godina nije prijestupna")