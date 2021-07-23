import numpy as np
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from math import sin, exp
from scipy.optimize import minimize

def f(x):
    return sin(x/5) * exp(x / 10) + 5 * exp(-x / 2)

res = minimize(f, 3, bounds=[(1, 30)])
# method='nelder-mead', options={'xatol': 1e-8, 'disp': True})


res = minimize(f, 2, bounds=[(1, 30)], method='BFGS')
print(f(res.x))

x = np.arange(1, 30, 0.05)
y = list(map(f, x))
print(y)

plt.plot(x, y)
plt.show()
