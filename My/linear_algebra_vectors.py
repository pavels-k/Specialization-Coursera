from sympy import diff, symbols, cos, sin, solve
from sympy.plotting import plot
import numpy as np



x = symbols('x')
def f(x):
    return x**2 + 2*x+1

f_diff = diff(f(x))

a = np.array([0, 5, -1])
b = np.array([-4, 9, 3])

print(f_diff.evalf(subs={x:1}))
print(diff(diff(f(x))))
print('Скалярное произведение a и b (через функцию):', np.dot(a, b))
print('Скалярное произведение a и b (через функцию):', a*b)

