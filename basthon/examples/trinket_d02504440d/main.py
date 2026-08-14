from pylab import *

N0 = 100             # Harer ved t = 0
N = N0
t = 0                # Starttid i måneder
t_slutt = 12*5       # Tid i måneder
dt = 1               # Tidssteg mellom hver simulering
k = 0.05*dt          # Vekstrate per måned

# Arrayer
harer = []
tid = []

harer.append(N0)
tid.append(t)

# Beregningsløkke
while t < t_slutt:
    N = N + k*N
    t = t + dt
    harer.append(N)
    tid.append(t)

scatter(tid,harer)
show()