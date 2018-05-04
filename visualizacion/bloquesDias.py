import pandas as pd 
import seaborn as sns 

df = pd.read_csv("bloquesDias.dat",delimiter = ";")
# temp = temp.pivot("month", "year", "passengers")

labs = [
"W",
"M",
"L",
"S",
"C",
"B",
"Z",
"O",
"R",
"Y",
"G",
"S",
"K",
"Q",
"M"
]

df["Bloque"] = labs
df = df.set_index("Bloque")

print(df)
ax = sns.heatmap(df, linewidths=.5)
fig = ax.get_figure()
fig.savefig("solDias.png")
