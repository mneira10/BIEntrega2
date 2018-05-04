import pandas as pd 
import pandas_profiling


df=pd.read_csv("./FINALDEVERITAS.csv",delimiter = "|",encoding = "iso8859_2")
profile = pandas_profiling.ProfileReport(df)
profile.to_file(outputfile="ofinalutput.html")