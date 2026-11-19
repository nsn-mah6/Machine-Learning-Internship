import numpy as np
print("-----Slicing and Indexing:-----")
values = np.array([10, 20, 30, 40, 50, 60])
print(values[0])
print(values[-1])
print(values[1:4])
print(values[::2])

matrix = np.array([[10, 20, 30], 
                   [40, 50, 60], 
                   [70, 80, 90]])
print(matrix)
print(matrix[0, :])
print(matrix[:, 1])
print( matrix[:2, 1:])



arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print(arr)
print(arr[0, :])
print(arr[2, :])
print(arr[:, 0])
print(arr[:, 2])
print(arr[0:2, :])
print(arr[:, 1:3])
print(arr[1:3, 1:3])
print(arr[::-1, :])
print(arr[:, ::-1])
print(arr[::-1, ::-1])
print(arr[0, 0])  
print(arr[1, 2])  
print(arr[3, 1])  



# Boolean indexing
print("-----Boolean Indexing:-----")
val = np.array([10, 20, 30, 40, 50, 60])

print(val[val > 30])
print(val[val < 40])
print(val[val >= 30])