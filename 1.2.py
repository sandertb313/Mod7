def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a%b
    return a



def frac(a,b):
    divisor = gcd(a, b)
    while (gcd(a, b) != 1 and b != 0):
        a, b = a / divisor, b / divisor
        divisor = gcd(a, b)
    return a, b, gcd(a, b)

print(frac(12, 9))


