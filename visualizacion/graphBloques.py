import numpy as np
import pandas as pd 
import seaborn as sns

df = pd.read_csv("/home/mauro/Documents/U/8vo/Inteligencia de negocios/proyecto2/BIEntrega2/visualizacion/bloques.dat",delimiter=  ";")
axa = sns.barplot(x="Bloque", y="Número de solicitudes", data=df,palette="Blues_d").set_title("Número de solicitudes por bloque")
# axa.set_xticklabels(axa.get_xticklabels(),rotation=30)
# print(df)
fig = axa.get_figure()
fig.savefig("solBloques.png")