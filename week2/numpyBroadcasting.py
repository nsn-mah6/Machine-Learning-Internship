import numpy as np

prices = np.array([100, 200, 300, 400])
print("Prices minus 10:", prices - 10)

monthly_sales = np.array([[100, 200, 300], [150, 250, 350]])
adjustment = np.array([10, 20, 30])
print("Column-wise adjustment:\n", monthly_sales + adjustment)