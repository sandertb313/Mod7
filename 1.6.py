def fact(n):
    res = 1
    while n > 1:
        res = res * n
        n -= 1

    return res

print(fact(10))

def binom(n, k):
    res = 0
    if (n >= k >= 1):
        res = fact(n) / (fact(n-k) * fact(k))

    return res

print (binom(40, 2))
