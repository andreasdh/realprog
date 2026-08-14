import pandas as pd
import seaborn as sns

fotballdata = pd.read_csv("eliteserien2023.txt", delimiter = ",")

# Til oppgave 5
sns.catplot(data=fotballdata, x="mål_hjemme", y="hjemmelag", kind="violin")

# Til oppgave 7
glimt_hjemme = fotballdata[fotballdata["hjemmelag"] == "Bodø/Glimt"]