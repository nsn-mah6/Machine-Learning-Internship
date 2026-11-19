import pandas as pd

print("-----Loading Dataset:-----")
df = pd.read_csv("data/messy_retail_sales.csv")
print("dataset loaded successfully")

print("filtering data based on city and product")
# City names have inconsistent spaces/capitalisation in the raw data.
kathmandu = df[df["City"].astype(str).str.strip().str.lower() == "kathmandu"]
print(kathmandu)

laptops = df[df["Product"] == "Laptop"]
print(laptops)

quantity_num = pd.to_numeric(df["Quantity"], errors="coerce")
print(df[quantity_num > 1])

# sorting
print("-----Sorting DataFrame:-----")
print(df.sort_values("City"))
print(df.sort_values(["Product", "Order_Date"], ascending=[True, True]))