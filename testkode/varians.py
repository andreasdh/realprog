import pandas as pd

soldata = pd.read_csv("../docs/datafiler/solflekker.txt", delimiter="\t")

flekkdata = soldata["Solflekker"]
n = len(flekkdata) # antall målinger

sum = 0
for flekker in flekkdata:
    sum += flekker
snitt = sum/n
print("Gjennomsnitt:", round(snitt, 1))

sum_avvik = 0
for flekker in flekkdata:
    sum_avvik += (flekker - snitt) # positivt over snitt, negativt under snitt
snitt_avvik = sum_avvik/n
print("Gjennomsnittlig avvik:", round(snitt_avvik, 1))

sum_avvik_2 = 0
for flekker in flekkdata:
    sum_avvik_2 += (flekker - snitt)**2 # alltid positivt
snitt_avvik_2 = sum_avvik_2/n # gjennomsnittlig kvadratavvik i DATASETTET vårt
print("Gjennomsnittlig kvadratavvik:", round(snitt_avvik_2, 1))

varians = sum_avvik_2/(n-1) # (estimert) gjennomsnittlig kvadratavvik i HELE POPULASJONEN
# hvorfor (n-1)?
# https://en.wikipedia.org/wiki/Bessel%27s_correction#Proof_of_correctness_%E2%80%93_Alternative_1
print("Varians:", round(varians, 1))
print("Standardavvik:", round(varians**0.5, 1))