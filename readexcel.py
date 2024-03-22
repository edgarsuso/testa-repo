import pandas as pd

#read excel table

filePath = "/home/ek/Downloads/5305_1.xls"

df = pd.read_excel(filePath)

print(df.head())