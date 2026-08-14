startbeløp = 25000
rente = 1
vekstfaktor = 1 + rente
beholdning = startbeløp 
år = 0

while beholdning <= startbeløp/2:
    beholdning = rente*beholdning
    år = år + 1

print(år)