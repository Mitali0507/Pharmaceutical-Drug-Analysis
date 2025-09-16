import pandas as pd

df=pd.read_csv("indian_pharmaceutical_products_clean.csv")

#cleaning and manipulating data
"""as these 3 columns have lots of null values, these steps will fill them
"""
#need to assign back columns as 'inplace' was not working

df["pack_size"]=df["pack_size"].fillna(df["pack_size"].median())
df["pack_unit"]=df["pack_unit"].fillna('unknown')
df["primary_strength"]=df["primary_strength"].fillna('not specified')

print(df.isnull().sum()) # shows the total null values in each column