import pandas as pd

#loading dataset
print("-----Loading Dataset:-----")
df = pd.read_csv("data/messy_retail_sales.csv")
df.head()

print("-----DataFrame Info:-----")
print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.columns.to_list())
print(df.describe())