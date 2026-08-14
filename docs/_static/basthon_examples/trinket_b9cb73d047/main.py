from pylab import *

# Koeffisientene i en andregradsfunksjon
a = 1   
b = 0
c = -4

x = linspace(-5,5,1000) # Lager 1000 x-verdier mellom -5 og 5
y = a*x**2 + b*x + c    # Lager y-verdier som tilsvarer hver x

plot(x,y)                   # Plotter grafen
xlabel('x')                 # Lager x-aksetittel
ylabel('y')                 # Lager y-aksetittel
axhline(y=0, color='black') # Lager x-akse
axvline(x=0, color='black') # Lager y-akse
grid()                      # Lager rutenett
show()                      # Viser grafen