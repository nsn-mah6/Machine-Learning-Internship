
import numpy as np

# Create an array from 5 to 50, increasing by 5
arr = np.arange(5, 51, 5)
print("Original Array:")
print(arr)

# Select the third and fourth elements
print("\nThird and Fourth Elements:")
print(arr[2:4])

# Create a 3 × 3 array and select the second row
arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\n3 × 3 Array:")
print(arr_2d)

print("\nSecond Row:")
print(arr_2d[1])

# Add 100 to every element using broadcasting
new_arr = arr + 100

print("\nArray after adding 100:")
print(new_arr)

# Calculate mean and median
print("\nMean:", np.mean(arr))
print("Median:", np.median(arr))
