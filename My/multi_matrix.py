import numpy as np

A = np.array([ [1, 2, 4, 29],
        [3, 4, 6, 1] ])

# умножение матрицы на число
A = A * 2
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()  
