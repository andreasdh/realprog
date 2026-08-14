a = 1     # første tall i tallfølgen
ledd = 10 # antall ledd i tallfølgen

for n in range(ledd-1):
  a = a + 2*n + 2
  
print("Ledd nummer", ledd, "er:", a)