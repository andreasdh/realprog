startbeløp = 25000
rente = 5  
vekstfaktor = 1 + rente/100
beholdning = startbeløp 
år = 0
tid_slutt = 10

while år <= tid_slutt:
    beholdning = vekstfaktor*beholdning
    år = år + 1

print(beholdning)