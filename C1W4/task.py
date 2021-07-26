from scipy.stats import chi2, norm
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(1, 1)
color = next(ax._get_lines.prop_cycler)["color"]

# df = 78
# x = np.linspace(gamma.ppf(0.01, df),
#                 gamma.ppf(0.99, df), 100)
# ax.plot(x, gamma.pdf(x, df),
#        'r-', lw=5, alpha=0.6, label='gamma pdf')
# x = np.linspace(20, 150, 100)
# pdf = chi2.pdf(x, df)
# plt.legend()
# plt.ylabel('$f(x)$')
# plt.xlabel('$x$')

# plt.hist(r, bins=10, density=True, color=color, edgecolor=color, fc="None")
# plt.plot(x, pdf, label='theoretical pdf', c = 'y')

# plt.show()
# np.show()


df = 78
r = chi2.rvs(df, size=1000)
# print(r.sum()/1000)

n_value = [5, 10, 50]
dlist = [[],[],[]]
for index, n in enumerate(n_value):
    s = 0
    for i in range(1000):
        r = chi2.rvs(df, size=n)
        N = np.mean(r)
        dlist[index].append(N)
print(dlist[0])

mu = df
sigma = np.sqrt(2*df/5)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

plt.plot(x, norm.pdf(x, mu, sigma))
plt.hist(dlist[0], density=True, color=color, edgecolor=color, fc="None")
plt.show()

sigma = np.sqrt(2*df/10)
plt.plot(x, norm.pdf(x, mu, sigma))
plt.hist(dlist[1], bins=10, density=True, color=color, edgecolor=color, fc="None")
plt.show()

sigma = np.sqrt(2*df/50)
plt.plot(x, norm.pdf(x, mu, sigma))
plt.hist(dlist[2], bins=10, density=True, color=color, edgecolor=color, fc="None")

plt.show()
