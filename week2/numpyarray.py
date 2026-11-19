import numpy as np

# Creating a one-dimensional array
numbers = np.array([10, 20, 30, 40, 50])
print("-----One-dimensional array:-----")
print(numbers)
print(type(numbers))


# Creating a two-dimensional array
data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print("-----Two-dimensional array:-----")
print(data)
print(type(data))

# Understanding array properties
print("-----Array Properties:-----")

data2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Dimensions:", data2.ndim)
print("Shape:", data2.shape)
print("Size:", data2.size)
print("Data type:", data2.dtype)

# NumPy functions
print("-----NumPy Functions:-----")
print(np.zeros(5))
print(np.ones(5))
print(np.arange(1, 11))
print(np.linspace(1, 10, 5))