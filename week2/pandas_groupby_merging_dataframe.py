import pandas as pd

print("-----Loading Dataset:-----")
df = pd.read_csv("data/messy_retail_sales.csv")
print("dataset loaded successfully")

print("-----Groupby and Aggregation of DataFrame:-----")
temp = df.copy()
temp["Quantity_num"] = pd.to_numeric(temp["Quantity"], errors="coerce")
temp["Unit_Price_num"] = pd.to_numeric(
    temp["Unit_Price"].astype(str).str.replace(",", "", regex=False),
    errors="coerce"
)
temp["Line_Total"] = temp["Quantity_num"] * temp["Unit_Price_num"]

print("-----Grouping by City:-----")
print(temp.groupby("City", dropna=False)["Order_ID"].count().sort_values(ascending=False))
print("-----Grouping by Category:-----")
print(temp.groupby("Category", dropna=False).agg(
    order_count=("Order_ID", "count"),
    total_quantity=("Quantity_num", "sum"),
    total_sales=("Line_Total", "sum")
))

print("-----Merging DataFrames:-----")
product_info = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Chair", "T-Shirt", "Keyboard",
                "Table", "Jeans", "Headphones", "Jacket", "Monitor", "Desk"],
    "Department": ["Computing", "Accessories", "Furniture", "Apparel",
                   "Accessories", "Furniture", "Apparel", "Accessories",
                   "Apparel", "Computing", "Furniture"]
})
merged = df.merge(product_info, on="Product", how="left")
print(merged.head(10))
print("Rows without product match:", merged["Department"].isna().sum())