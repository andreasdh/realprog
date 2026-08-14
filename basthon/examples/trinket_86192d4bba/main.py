"""
Program 2 skal skrive ut hvorvidt en gitt andregradslikninger har to, én eller ingen reelle løsninger.
Du kan gjerne utvide programmet til slutt slik at:
1. Programmet skriver ut hva løsningene er.
2. Andregradsformelen implementeres som en Python-funksjon.
"""
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a == 0:
  # Fyll inn her
else:
  rotuttrykk = b**2 - 4*a*c
  if rotuttrykk > 0:
    print("Likningen har to løsninger")
  elif # Fyll inn her
  else:
    print("Likninger har én løsning")