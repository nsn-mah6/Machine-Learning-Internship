import numpy as np
import pandas as pd

# NumPy: arrays and vectorized calculations
scores = np.array([70, 80, 90, 60, 85])
print("Scores:", scores)
print("Mean:", np.mean(scores))
print("Maximum:", np.max(scores))
print("Scores + 5:", scores + 5)

# pandas: create and inspect a DataFrame
data = {
    "name": ["Nishan", "Mohan", "Salina", "Sabita"],
    "marks": [85, 45, 92, 78],
    "department": ["IT", "Data", "IT", "AI"]
}
df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)
print("\nFirst rows:")
print(df.head())
print("\nSummary:")
print(df.describe)
print("\nStudents who passed:")
print(df[df["marks"] >= 50])
print("\nAverage marks by department:")
print(df.groupby("department")["marks"].mean())