def Fibonacci():
    res = 0
    a = 0
    b = 1
    c = 0
    while (a < 4000000):
        c = a + b
        if (c % 2 == 0):
            res += c
        a = b
        b = c

    return res

print(Fibonacci())