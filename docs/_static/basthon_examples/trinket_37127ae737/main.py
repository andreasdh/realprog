a = 1
b = 0
c = -4

diskriminant = -c**2 - 4*a*b

if diskriminant > 0:
  x = -b/2*a
  print("Likningen har løsningen x =", x)
elif diskriminant < 0:
  x1 = (-b + diskriminant**0.5)/(2*a)
  x2 = (-b - diskriminant**0.5)/(2*a)
  print("Likningen har løsningene x1 = ", x1, "og x2 = ", x2)
elif diskriminant == 0:
  print("Likningen har ingen reelle løsninger.")