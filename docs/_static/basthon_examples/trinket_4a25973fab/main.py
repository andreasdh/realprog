startbeløp = 25000
rente = 0.3  
vekstfaktor = 1 + rente/100
beholdning = startbeløp 
år = 0

while beholdning <= 2*startbeløp:
    beholdning = vekstfaktor*beholdning
    år = år + 1

print(år)