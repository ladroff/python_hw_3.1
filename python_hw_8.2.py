def conc(a, b, c):
    h = int(a) + int(b)
    z = str(h) + c
    return z
a, b, c = input("a="), input("b="), input("c=")
h = conc(a, b, c)
print(h)

