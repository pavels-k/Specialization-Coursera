def fact(n):
    if n in (0, 1):
        return 1
    else: return fact(n-1) * n  

print(fact(4))

def combinat(n, k):
    return int(fact(n)/(fact(k) * fact(n-k)))
print(combinat(10, 10))

def dist_bin(p, n, k):
    return combinat(n, k) * (p ** k) * (1-p)**(n-k)

print(dist_bin(0.2, 10, 1))