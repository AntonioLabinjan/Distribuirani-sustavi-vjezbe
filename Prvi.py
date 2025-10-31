broj1 = int(input("Unesi prvi broj: "))
broj2 = int(input("Unesi drugi broj: "))
operator = input("Unesi operator: ")

if operator == "+":
  print(broj1 + broj2)
elif operator == "-":
  print(broj1 - broj2)
elif operator == "*":
  print(broj1 * broj2)
elif operator == "/":
  print(broj1 / broj2)
else:
  print("Pogrešan operator")