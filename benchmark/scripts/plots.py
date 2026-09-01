
## codon optimization


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_excel("full_data.xlsx")


sns.set(style="whitegrid", context="talk")



fig = plt.figure(figsize=(10,6))
sns.barplot(x="sequence_var", y="GC", data=df, palette="Set2", ci="sd", edgecolor="black")
sns.stripplot(x="sequence_var", y="GC", data=df, color="black", size=6, jitter=True)
plt.title("GC%")
plt.ylabel("GC [%]")
plt.xlabel("Sequence")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()

fig.savefig(f'optimization_GC.svg', dpi = 300)


fig = plt.figure(figsize=(10,6))
sns.barplot(x="sequence_var", y="freq", data=df, palette="Set2", ci="sd", edgecolor="black")
sns.stripplot(x="sequence_var", y="freq", data=df, color="black", size=6, jitter=True)
plt.title("Codon Frequency")
plt.ylabel("Codon Frequency")
plt.xlabel("Sequence")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()

fig.savefig(f'optimization_freq.svg', dpi = 300)

 



fig = plt.figure(figsize=(10,6))
sns.barplot(x="sequence_var", y="MEF", data=df, palette="Set2", ci="sd", edgecolor="black")
sns.stripplot(x="sequence_var", y="MEF", data=df, color="black", size=6, jitter=True)
plt.title("Minimum Free Energy (MFE)")
plt.ylabel("MFE [kcal/mol]")
plt.xlabel("Sequence")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()

fig.savefig(f'optimization_MEF.svg', dpi = 300)




