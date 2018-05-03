import pandas as pd 
import pandas_profiling


df=pd.read_csv("./datosPipeline2.csv",delimiter = "|",encoding = "iso8859_2")
profile = pandas_profiling.ProfileReport(df)
profile.to_file(outputfile="perfilamiento.html")