from scipy.stats import poisson

mu = 3
print(1- poisson.pmf(0, mu)- poisson.pmf(1, mu)- poisson.pmf(2, mu)- poisson.pmf(3, mu)- poisson.pmf(4, mu))