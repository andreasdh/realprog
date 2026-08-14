bakterier = 100
antall_timer = 30
vekst = 0.42

for i in range(antall_timer):
    bakterier = bakterier + bakterier*vekst

print(int(bakterier))
