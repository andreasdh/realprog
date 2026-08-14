from pylab import exp, log10, linspace

x = linspace(0,100,10000)
y = exp(-x) + x + 5 - log10(0.006*x + 1) - x**0.3 - 10

for i in range(len(y)-1):
  if # fyll inn her
