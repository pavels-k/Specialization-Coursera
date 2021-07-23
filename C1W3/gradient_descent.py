import numpy as np
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import math

e = 2.7

x, y = symbols('x y')
f = 2*(x**2)*(y**3) + 3*(x**4) + 5*y - 7

print(f)


grad = np.array([diff(f, x), diff(f, y)])
print(grad)


x_n = np.array([40, 40])


print()
x_next = x_n
for i in range(5):
    grad_n = np.array([grad[0].evalf(
        subs={x: x_n[0], y:x_n[1]}), grad[1].evalf(subs={x: x_n[0], y:x_n[1]})])
    print(grad_n)
    x_n = x_next
    x_next = x_n - 1 * grad_n
    print(x_next)

# fig = plt.figure()
# ax = fig.add_subplot(1,1,1,projection="3d")
# x,y = np.meshgrid(np.linspace(-5,5,100), np.linspace(-5,5,100))
# z = 2*(x**2)*(y**3) + 3*(x**4) + 5*y - 7
# ax.plot_surface(x,y,z)

# plt.show()
