def Palindromes():
    palproduct = ""
    pal = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            res = i * j
            if str(res) == str(res)[::-1] and res > pal:
                palproduct = str(i) + "* "+  str(j)
                pal = res

    return palproduct, pal

print(Palindromes())
