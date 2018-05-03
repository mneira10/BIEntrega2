import pandas as pd 
import pandas_profiling


df=pd.read_csv("./subirsalones_2018-1.csv",delimiter = ";",encoding = "iso8859_2")
profile = pandas_profiling.ProfileReport(df)
profile.to_file(outputfile="perfilamientoSalonesGerenciaCampus.html")