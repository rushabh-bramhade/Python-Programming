import numpy as np 

arr = np.array([
    [2,3,4,1,4],[1,2,34,5,6]
    ])

for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        print(arr[i][j],end=" ")
    print()

