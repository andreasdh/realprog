t_slutt = 1   # slutt-tid i s
t = 0         # starttid i s
dt = 1E-8     # tidssteg i s
s = 0         # startposisjon i m
v = 0         # startfart i m/s
g = 9.8        # tyngdeakselerasjonen i m/s^2

while t < t_slutt:
  a = -g
  v = v + a*dt
  s = s + v*dt + 0.5*a*dt**2
  t = t + dt

print("Ballen falt", s, "meter.")