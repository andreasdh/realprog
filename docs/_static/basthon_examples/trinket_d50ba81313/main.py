from pylab import exp, log10

x0 = 0   # Startpunkt
dx = 1E-3  # Forskjellen mellom x-verdier

# Definerer funksjonen
def f(t):
    return exp(-t) + t + 5 - log10(0.006*t + 1) - t**0.3 - 10

x1 = x0    # Velger første x-verdi
x2 = x1+dx # Velger andre x-verdi
while f(x1)*f(x2) > 0:
    x1 = x2
    x2 = x1+dx
    
x = (x2+x1)/2
print("x =", x)
