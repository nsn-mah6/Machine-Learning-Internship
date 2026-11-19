import pandas as pd

#loading dataset
print("-----Loading Dataset:-----")
df = pd.read_csv("data/messy_retail_sales.csv")
df.head()

print("-----DataFrame Info:-----")
print(df.head()) # Display first 5 rows
print(df.tail()) # Display last 5 rows
print(df.shape) # Display dimensions
print(df.info()) # Display information about the DataFrame
print(df.columns.to_list()) # Display column names
print(df.describe()) # Display summary statistics

print(df.isnull().sum()) # Display missing values count for each column
# Convert numerical columns into numeric data types
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce")

# Fill missing numerical values with their column mean
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())
df["Unit_Price"] = df["Unit_Price"].fillna(df["Unit_Price"].mean())

# Fill missing categorical values with their mode
for col in df.select_dtypes(include="object").columns:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])

print("\n-----Missing Values After Cleaning:-----")
print(df.isnull().sum())



print(df.duplicated().sum()) # Display number of duplicate rows

df = df.drop_duplicates()

print("\n-----Duplicate Rows After Removing:-----")
print(df.duplicated().sum())