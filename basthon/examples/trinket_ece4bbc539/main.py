from pylab import *

x = linspace(-5, 6, 1000) # Lager x-verdier
y = x**2 - x + 1          # Lager tilsvarende y-verdier

plot(x,y) # Plotter funksjonen
grid()    # Skrur på rutenett
show()    # Viser plottet