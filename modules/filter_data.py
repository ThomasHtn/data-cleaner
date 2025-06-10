import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from utils.outliers import outliners_filter

# Load CSV
df = pd.read_csv("data/data.csv")


############### FILTER AND REPLACE VALUE #############

# Keep columns and remove :
# - historique_credit, 
# - score_credit,
# - montant_pret 
df = df[[
    'age', 
    'taille', 
    'poids', 
    'revenu_estime_mois', 
    'risque_personnel',
    'loyer_mensuel',
    'montant_pret',
]]

# Replace "na" (empty) by mean
df.fillna({'revenu_estime_mois': df['revenu_estime_mois'].mean()}, inplace=True)
df.fillna({'age': df['age'].mean()}, inplace=True)
df.fillna({'taille': df['taille'].mean()}, inplace=True)
df.fillna({'risque_personnel': df['risque_personnel'].mean()}, inplace=True)
df.fillna({'loyer_mensuel': df['loyer_mensuel'].mean()}, inplace=True)
df.fillna({'montant_pret': df['montant_pret'].mean()}, inplace=True)


df = df.dropna() # Remove missing row value from other columns
df = df.drop_duplicates() # Remove duplicated row

df = df[df['age'] <= 80] # Cannot get loan after this age
df = df[df['age'] >= 18] # must be adult

# display result
print(df.describe)


############### DETECT DATA ERROR (Boxplot) ###############
print("BOXPLOT : revenu_estime_mois")
sns.boxplot(x=df['revenu_estime_mois'])
plt.show()
df2 = outliners_filter(df, 'revenu_estime_mois')
df = df2
print("UPDATED BOXPLOT : revenu_estime_mois")
sns.boxplot(x=df['revenu_estime_mois'])
plt.show()


print("BOXPLOT : age")
sns.boxplot(x=df['age'])
plt.show()


print("BOXPLOT : taille")
sns.boxplot(x=df['taille'])
plt.show()
df2 = outliners_filter(df, 'taille')
df = df2
print("UPDATED BOXPLOT : taille")
sns.boxplot(x=df['taille'])
plt.show()


print("BOXPLOT : poids")
sns.boxplot(x=df['poids'])
plt.show()
df2 = outliners_filter(df, 'poids')
df = df2
print("UPDATED BOXPLOT : poids")
sns.boxplot(x=df['poids'])
plt.show()


print("BOXPLOT : risque_personnel")
sns.boxplot(x=df['risque_personnel'])
plt.show()


print("BOXPLOT : loyer_mensuel")
sns.boxplot(x=df['loyer_mensuel'])
plt.show()
df2 = outliners_filter(df, 'loyer_mensuel')
df = df2
print("UPDATED BOXPLOT : loyer_mensuel")
sns.boxplot(x=df['loyer_mensuel'])
plt.show()


print("BOXPLOT : montant_pret")
sns.boxplot(x=df['montant_pret'])
plt.show()
df2 = outliners_filter(df, 'montant_pret')
df = df2
print("UPDATED BOXPLOT : montant_pret")
sns.boxplot(x=df['montant_pret'])
plt.show()


df = df.drop_duplicates() # Remove duplicated row
print(df.describe)

############### SEABORN ###############
sns.set_theme(style="darkgrid")
sns.histplot(df['revenu_estime_mois'], kde=True)
plt.legend() 
plt.show()


sns.set_theme(style="darkgrid")
sns.histplot(df['montant_pret'], kde=True)
plt.legend() 
plt.show()


### SAVE FILTERED CSV
df.to_csv('data/out.csv', index=False)  