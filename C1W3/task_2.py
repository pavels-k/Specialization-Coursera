from scipy import optimize
from math import sin, exp

def f(x):
    return sin(x/5) * exp(x / 10) + 5 * exp(-x / 2)
res = optimize.differential_evolution(f, bounds = [(1,30)])
print(round(f(res.x), 2))

print(res.nfev) # количество вычислений значения функции 
print(res.nit) # количество итераций