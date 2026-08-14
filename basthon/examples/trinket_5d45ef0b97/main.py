from pylab import *

def f(x):
  return x - 4
  
def g(x):
  return -x + 3
  
x = linspace(-3,5,100) # Lager en array (en slags liste) med 100 verdier jevnt fordelt mellom -3 og 3
y1 = f(x) # lager en ny array med funksjonsverdiene til f for alle verdiene i x
y2 = g(x) # lager en ny array med funksjonsverdiene til g for alle verdiene i x

plot(x, y1, label = "f", color = "hotpink") # plotter verdiene i y1 mot x
plot(x, y2, label = "g", color = "salmon")  # plotter verdiene i y2 mot x

axhline(y = 0, color = "black") # horisontal linje på y = 0
axvline(x = 0, color = "black") # vertikal linje på x = 0

ylim(-10, 10) # verdimengde
xlim(-5, 7)   # definisjonsmengde

xlabel("x")   # x-aksetittel
ylabel("y")   # y-aksetittel

legend() # setter på merkelappene (labels)
grid()   # lager rutenett
show()   # viser plottet