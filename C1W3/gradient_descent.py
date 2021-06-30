import numpy as np
from sympy import *

x, y = symbols('x y')
f = 2*(x**2)*(y**3) + 3*(x**4) + 5*y - 7

print(f)
print(diff(f, x))
print(diff(f, y))