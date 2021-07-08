import numpy as np
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from math import sin, exp
from scipy.optimize import minimize, differential_evolution

def f(x):
    return int(sin(x/5) * exp(x / 10) + 5 * exp(-x / 2))

res = minimize(f, 3, bounds=[(1, 30)])



res = minimize(f, 30, bounds=[(1, 30)], method='BFGS')
print(f(res.x))

res = differential_evolution(f, bounds = [(1,30)])
print(round(f(res.x), 2))

x = np.arange(1, 30, 0.05)
y = list(map(f, x))
#print(y)

plt.plot(x, y)
plt.show()