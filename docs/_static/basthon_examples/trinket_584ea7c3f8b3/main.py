import pandas as pd

soldata = pd.read_csv("solflekker.txt", delimiter="\t")

flekkdata = soldata["Solflekker"]
n = len(flekkdata) # antall målinger

sum = 0
for flekker in flekkdata:
    sum += flekker
    
snitt = sum/n
print("Gjennomsnitt:", round(snitt, 1))