# Statistikk: Antall mål, stddev, mål hjemme/borte Eliteserien 2023

import matplotlib.pyplot as plt # trengs ikke på trinket?
#import numpy as np
#from scipy.stats import norm
import pandas as pd
import seaborn as sns

fotballdata = pd.read_csv("eliteserien2023.txt", delimiter = ",")

# Oppgave 1: Finn snitt og standarddavvik for mål til hjemmelaget og bortelaget
print(fotballdata.describe())

'''
snitt_hjemme = fotballdata["mål_hjemme"].mean()                           # gjennomsnitt
standardavvik_hjemme = fotballdata["mål_hjemme"].std()                    # estimert standardavvik
min_hjemme = fotballdata["mål_hjemme"].min()
maks_hjemme = fotballdata["mål_hjemme"].max()
x_hjemme = np.arange(min_hjemme, maks_hjemme, 0.001)
y_hjemme = norm.pdf(x_hjemme, snitt_hjemme, standardavvik_hjemme)

snitt_borte = fotballdata["mål_borte"].mean()                           # gjennomsnitt
standardavvik_borte = fotballdata["mål_borte"].std()                    # estimert standardavvik
min_borte = fotballdata["mål_borte"].min()
maks_borte = fotballdata["mål_borte"].max()
x_borte = np.arange(min_borte, maks_borte, 0.001)
y_borte = norm.pdf(x_borte, snitt_borte, standardavvik_borte)

plt.plot(x_hjemme, y_hjemme, label="mål hjemme")
plt.plot(x_borte, y_borte, label="mål borte")
plt.legend()
plt.show() # trengs ikke på trinket?
'''

# Oppgave 2: Hvilke lag scoret og slapp inn mest hjemme? Og borte?

sns.catplot(data=fotballdata, x="mål_hjemme", y="hjemmelag", kind="violin")
plt.show() # trengs ikke på trinket?

sns.catplot(data=fotballdata, x="mål_borte", y="hjemmelag", kind="violin")
plt.show() # trengs ikke på trinket?

sns.catplot(data=fotballdata, x="mål_hjemme", y="bortelag", kind="violin")
plt.show() # trengs ikke på trinket?

sns.catplot(data=fotballdata, x="mål_borte", y="bortelag", kind="violin")
plt.show() # trengs ikke på trinket?

# Oppgave 3: Hvilke resultater er mest vanlige totalt sett?

sns.kdeplot(data=fotballdata, x="mål_borte", y="mål_hjemme", fill="true")
plt.xlim(0, 5)
plt.ylim(0, 7)
plt.show() # trengs ikke på trinket?

# Oppgave 4: Hvilke resultater er mest vanlige når Bodø/Glimt og TIL spiller hjemme / borte?

glimt_hjemme = fotballdata[fotballdata["hjemmelag"] == "Bodø/Glimt"]
til_hjemme = fotballdata[fotballdata["hjemmelag"] == "Tromsø"]
glimt_borte = fotballdata[fotballdata["bortelag"] == "Bodø/Glimt"]
til_borte = fotballdata[fotballdata["bortelag"] == "Tromsø"]

sns.kdeplot(data=glimt_hjemme, x="mål_borte", y="mål_hjemme", label="Bodø/Glimt hjemme", fill="true")
plt.legend()
plt.xlim(0, 5)
plt.ylim(0, 7)
plt.show() # trengs ikke på trinket?

sns.kdeplot(data=til_hjemme, x="mål_borte", y="mål_hjemme", label="Tromsø hjemme", fill="true")
plt.legend()
plt.xlim(0, 5)
plt.ylim(0, 7)
plt.show() # trengs ikke på trinket?

sns.kdeplot(data=glimt_borte, x="mål_borte", y="mål_hjemme", label="Bodø/Glimt borte", fill="true")
plt.legend()
plt.xlim(0, 5)
plt.ylim(0, 7)
plt.show() # trengs ikke på trinket?

sns.kdeplot(data=til_borte, x="mål_borte", y="mål_hjemme", label="Tromsø borte", fill="true")
plt.legend()
plt.xlim(0, 5)
plt.ylim(0, 7)
plt.show() # trengs ikke på trinket?

print()