import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x/5)*np.exp(x/10) + 5 * np.exp(-x/2)


x = np.arange(start=0, stop=16, step=1)
y = list(map(f, x))
plt.plot(x, y)


A_1 = np.ones((2, 2))
A_1[0][1] = 1
A_1[1][1] = 15
b = np.array([f(1), f(15)])
w = np.linalg.solve(A_1, b)
aprox_1 = w[0] + w[1] * x
#plt.plot(x, aprox_1)


A_2 = np.ones((3, 3))
A_2[0][1] = 1
A_2[1][1] = 8
A_2[2][1] = 15

A_2[0][2] = 1
A_2[1][2] = 64
A_2[2][2] = 225

b = np.array([f(1), f(8), f(15)])
w = np.linalg.solve(A_2, b)
aprox_2 = w[0] + w[1] * x + w[2] * x**2
#plt.plot(x, aprox_2)


A_3 = np.ones((4, 4))
A_3[0][1] = 1
A_3[1][1] = 4
A_3[2][1] = 10
A_3[3][1] = 15

A_3[0][2] = 1
A_3[1][2] = 16
A_3[2][2] = 100
A_3[3][2] = 225


A_3[0][3] = 1
A_3[1][3] = 4**3
A_3[2][3] = 10**3
A_3[3][3] = 15**3

b = np.array([f(1), f(4), f(10), f(15)])
w = np.linalg.solve(A_3, b)
aprox_3 = w[0] + w[1] * x + w[2] * x**2 + w[3] * x**3
plt.plot(x, aprox_3)

w = [round(i, 2) for i in w]
print(w)


plt.show()
