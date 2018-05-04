import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
df = pd.read_csv("bloqAct.dat",delimiter = ";")
# temp = temp.pivot("month", "year", "passengers")
print(df)

df = df.set_index("Bloque")
sns.set(font_scale = 0.8)
ax = sns.heatmap(df, linewidths=.5)
# sns.set_context("paper", rc={"axes.labelsize":10})
ax.set_xlabel('Actividad')
fig = ax.get_figure()
# ax.set_xticklabels(ax.get_xticklabels(),rotation = 40,ha='right')

plt.tight_layout()
fig.savefig("bloqAct.png")
