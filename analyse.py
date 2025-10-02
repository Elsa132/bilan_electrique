import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("bilan-electrique-transpose.csv", sep=";")


print(df.head())

df["Jour"] = pd.to_datetime(df["Jour"], dayfirst=True)

df_jour = df.groupby("Jour")["Puissance moyenne journalière (W)"].mean()

plt.figure(figsize=(10,5))
plt.plot(df_jour.index, df_jour.values, label="Moyenne journalière")
plt.xlabel("Date")
plt.ylabel("Puissance moyenne (W)")
plt.title("Évolution de la puissance moyenne journalière")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("evolution_puissance.png")  # Sauvegarde du graphique
plt.show()

df_cat = df.groupby("Catégorie client")["Puissance moyenne journalière (W)"].mean()

plt.figure(figsize=(8,5))
df_cat.plot(kind="bar")
plt.xlabel("Catégorie client")
plt.ylabel("Puissance moyenne (W)")
plt.title("Puissance moyenne par catégorie client")
plt.tight_layout()
plt.savefig("puissance_par_categorie.png")
plt.show()
