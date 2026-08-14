from pylab import *

startkapital = 5000
penger = startkapital
år = 0
rente = 0.01
år_liste = [0]
penger_liste = [startkapital]

while penger < startkapital*2:
  penger = penger + penger*rente
  år = år + 1
  år_liste.append(år)
  penger_liste.append(penger)
  
# plott her