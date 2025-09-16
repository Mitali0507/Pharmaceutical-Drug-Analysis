import pandas as pd

df=pd.read_csv("indian_pharmaceutical_products_clean.csv")

print(df.head(10)) #prints preview upto 10 entries 
print(df.info())   #shows info like columns,non-null count, datatypes
print(df.describe()) #arithmetics of numeric columns



