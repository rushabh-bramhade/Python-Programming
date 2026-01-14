import numpy as np

n = int(input("How number do you want to store in 2d array :"))

arr = np.zeros((n, n), dtype=int)


for i in range(n):
    for j in range(n):
        arr[i][j] = int(input(f"Enter element at row {i+1}, column {j+1}: "))

print(arr)