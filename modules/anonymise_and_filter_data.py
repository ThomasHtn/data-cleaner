import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from utils.outliers import outliners_filter

# Load CSV
df = pd.read_csv("data/data_not_RGPD.csv")

############### SELECT & ANONYMISE DATASET #############

# Keep columns and remove :
# - historique_credit, ~ 50% of na value
# - score_credit, ~ 50% of na value
df = df[
    [
        "age",
        "taille",
        "poids",
        "sexe",
        "sport_licence",
        "niveau_etude",
        "region",
        "smoker",
        "nationalité_francaise",
        "revenu_estime_mois",
        "situation_familiale",
        "risque_personnel",
        "loyer_mensuel",
        "montant_pret",
    ]
]

# Replace "na" (empty) by mean
df.fillna({"situation_familiale": df["situation_familiale"].mode()}, inplace=True)
df.fillna({"loyer_mensuel": df["loyer_mensuel"].mean()}, inplace=True)


# Transform category to numeric

df = pd.get_dummies(df, columns=["sexe"])
df = pd.get_dummies(df, columns=["sport_licence"])
df = pd.get_dummies(df, columns=["niveau_etude"])
df = pd.get_dummies(df, columns=["region"])
df = pd.get_dummies(df, columns=["smoker"])
df = pd.get_dummies(df, columns=["nationalité_francaise"])
df = pd.get_dummies(df, columns=["situation_familiale"])


# display result
print(df.head())

############### DETECT DATA ERROR (Boxplot) ###############
print("BOXPLOT : revenu_estime_mois")
sns.boxplot(x=df["revenu_estime_mois"])
plt.show()
df2 = outliners_filter(df, "revenu_estime_mois")
df = df2
print("UPDATED BOXPLOT : revenu_estime_mois")
sns.boxplot(x=df["revenu_estime_mois"])
plt.show()


print("BOXPLOT : age")
sns.boxplot(x=df["age"])
plt.show()


print("BOXPLOT : taille")
sns.boxplot(x=df["taille"])
plt.show()
df2 = outliners_filter(df, "taille")
df = df2
print("UPDATED BOXPLOT : taille")
sns.boxplot(x=df["taille"])
plt.show()


print("BOXPLOT : poids")
sns.boxplot(x=df["poids"])
plt.show()
df2 = outliners_filter(df, "poids")
df = df2
print("UPDATED BOXPLOT : poids")
sns.boxplot(x=df["poids"])
plt.show()


print("BOXPLOT : risque_personnel")
sns.boxplot(x=df["risque_personnel"])
plt.show()


print("BOXPLOT : loyer_mensuel")
sns.boxplot(x=df["loyer_mensuel"])
plt.show()
df2 = outliners_filter(df, "loyer_mensuel")
df = df2
print("UPDATED BOXPLOT : loyer_mensuel")
sns.boxplot(x=df["loyer_mensuel"])
plt.show()


print("BOXPLOT : montant_pret")
sns.boxplot(x=df["montant_pret"])
plt.show()
df2 = outliners_filter(df, "montant_pret")
df = df2
print("UPDATED BOXPLOT : montant_pret")
sns.boxplot(x=df["montant_pret"])
plt.show()


df = df.drop_duplicates()  # Remove duplicated row

############### SEABORN ###############
sns.set_theme(style="darkgrid")
sns.histplot(df["revenu_estime_mois"], kde=True)
plt.legend()
plt.show()


sns.set_theme(style="darkgrid")
sns.histplot(df["montant_pret"], kde=True)
plt.legend()
plt.show()

### SAVE FILTERED CSV
df.to_csv("data/data_RGPD.csv", index=False)
