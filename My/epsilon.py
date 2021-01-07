from sympy import diff, symbols, cos, sin, solve

eps = 1.0
while eps+1 > 1:
    eps = eps / 2
eps = eps * 2

x = symbols('x')
def f(x):
    return x**2 + 2*x+1

print((f(1+eps)-f(1))/eps)