import math

def intdiv(a):
    list = []
    for i in range(1, a):
        if a % i == 0:
            list.append(i)

    return list


def isPrime(a):
    list = intdiv(a)
    if (len(list) == 1):
        return True
    return False


print(intdiv(100))
print(isPrime(6857))


def PrimeFactor(a):
    factors = []
    while a % 2 == 0:
        a = a / 2
        factors.append(2)
    for i in range(3, int(math.sqrt(a)) + 1, 2):
        if (a % i == 0):
            a = a / i
            factors.append(i)

    if a > 2:
        factors.append(a)

    return factors

print(PrimeFactor(600851475143))
