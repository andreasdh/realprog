# Statistikk: Antall mål, stddev, mål hjemme/borte Eliteserien 2023

import matplotlib.pyplot as plt # trengs ikke på trinket?
import numpy as np
from scipy.stats import norm
import pandas as pd
import seaborn as sns

fotballdata = pd.read_csv("eliteserien2023.txt", delimiter = ",")
print(fotballdata.describe())

snitt = fotballdata["mål_hjemme"].mean()                           # gjennomsnitt
standardavvik = fotballdata["mål_hjemme"].std()                    # estimert standardavvik
min = fotballdata["mål_hjemme"].min()
maks = fotballdata["mål_hjemme"].max()

x = np.arange(min, maks, 0.001)
plt.plot(x, norm.pdf(x, snitt, standardavvik), label="mål_hjemme")

snitt = fotballdata["mål_borte"].mean()                           # gjennomsnitt
standardavvik = fotballdata["mål_borte"].std()                    # estimert standardavvik
min = fotballdata["mål_borte"].min()
maks = fotballdata["mål_borte"].max()

#x = np.arange(min, maks, 0.001)
#plt.plot(x, norm.pdf(x, snitt, standardavvik), label="mål_borte")

#plt.legend()
#plt.show() # trengs ikke på trinket?

#sns.catplot(data=fotballdata, x="mål_hjemme", y="hjemmelag", kind="violin")
#plt.show() # trengs ikke på trinket?

sns.kdeplot(data=fotballdata, x="mål_hjemme", y="mål_borte", fill="true")
plt.xlim(0, 7)
plt.ylim(0, 5)
plt.show() # trengs ikke på trinket?

glimt_hjemme = fotballdata[fotballdata["hjemmelag"] == "Bodø/Glimt"]
til_hjemme = fotballdata[fotballdata["hjemmelag"] == "Tromsø"]

sns.kdeplot(data=glimt_hjemme, x="mål_hjemme", label="Bodø/Glimt")
sns.kdeplot(data=til_hjemme, x="mål_hjemme", label="Tromsø")
plt.legend()
plt.xlim(0, 7)
plt.show() # trengs ikke på trinket?

sns.kdeplot(data=glimt_hjemme, x="mål_borte", label="Bodø/Glimt")
sns.kdeplot(data=til_hjemme, x="mål_borte", label="Tromsø")
plt.legend()
plt.xlim(0, 7)
plt.show() # trengs ikke på trinket?

print()