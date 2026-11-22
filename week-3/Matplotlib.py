import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# DataFrame
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
expenses = [12000, 15000, 11000, 18000, 20000, 17000]

products = ["Laptop", "Mobile", "Tablet", "Headphones", "Keyboard"]
sales = [50, 80, 40, 65, 35]

marks = [
    45, 50, 55, 60, 65, 70, 75, 80,
    85, 90,
]

sales_2025 = [100, 120, 150, 130, 180, 200]
sales_2026 = [110, 140, 135, 160, 190, 220]

expenses = [12000, 15000, 11000, 18000]



# Line chart: Monthly Expenses
plt.figure(figsize=(8, 5))

plt.plot(months, expenses, marker="o", linewidth=2)

plt.title("Monthly Expenses")
plt.xlabel("Months")
plt.ylabel("Expenses (NPR)")

plt.grid(True)
plt.show()


# Bar chart: Product Sales
plt.figure(figsize=(9, 5))

bars = plt.bar(products, sales)

plt.title("Product Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Number of Sales")

# Display values above each bar
plt.bar_label(bars)

plt.show()


# Histogram: Student Marks
plt.figure(figsize=(8, 5))

plt.hist(marks, bins=5, edgecolor="black")

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.grid(axis="y", alpha=0.3)
plt.show()

# Multiple Lines: Sales Comparison
plt.figure(figsize=(9, 5))

plt.plot( months, sales_2025, marker="o", label="Sales 2025")

plt.plot( months, sales_2026, marker="s", label="Sales 2026")
plt.title("Monthly Sales Comparison: 2025 vs 2026")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.legend()
plt.grid(True)

plt.show()

# Subplots: Display Three Charts Together
# Create three subplots
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# First chart: Bar chart
axes[0].bar(products, sales)
axes[0].set_title("Product Sales")
axes[0].set_xlabel("Products")
axes[0].set_ylabel("Sales")
axes[0].tick_params(axis="x", rotation=45)

# Second chart: Line chart
axes[1].plot(months, expenses, marker="o")
axes[1].set_title("Monthly Expenses")
axes[1].set_xlabel("Months")
axes[1].set_ylabel("Expenses (NPR)")
axes[1].grid(True)

# Third chart: Histogram
axes[2].hist(marks, bins=5, edgecolor="black")
axes[2].set_title("Student Marks")
axes[2].set_xlabel("Marks")
axes[2].set_ylabel("Frequency")

plt.tight_layout()
plt.show()