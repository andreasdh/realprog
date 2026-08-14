a = 1
b = -2
c = 1

diskriminant = b**2 - 4*a*c

if diskriminant < 0:
  print("Likningen har ingen reelle løsninger.")
elif diskriminant > 0:
  print("Likningen har to reelle løsninger.")
elif diskriminant == 0:
  print("Likningen har én reell løsning.")