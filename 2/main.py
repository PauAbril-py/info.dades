
while True:
  b = input("que numero?")
  f = open('2/files/'+b, 'r')
  a = f.read()
  if a == "¡Has ganado! Enhorabuena":
    print(a)
    break
  else:
    print (a)