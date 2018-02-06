def encode(a, base):
    res = ""
    while (a != 0):
        residual = a % base;
        a = int(a / base)

        if (residual >= 0 and residual <= 9):
            res = str(residual) + res
        else :
            res = chr(residual + 87) + res
    return res


print (encode(4321, 16))

def decode(a, base):
    res = 0
    a = str(a)
    for i in range (0, len(str(a))):
        res += int(a[i], base) * (base ** (len(a) - 1 -i))
    return res

print (decode("10e1", 16))


def convert(stringa, fromk, tob):
    res = decode(stringa, fromk)
    res = encode(res, tob)
    return res

print (convert(10011010, 2, 4))
