import numpy as np
from scipy import linalg
from numpy.linalg import norm

A = np.array([[4, 5, 5, 3], [5, 3, 3, 5], [3, 5, 4, 4], [0, 0, 0, 0]])
# ,[3,5,4,4]])

b = np.array([1, 0, 1, 0])

#x = linalg.solve(A,b)
print('L1 норма вектора a:\n', np.linalg.norm(b, ord=1))
# lstsq
