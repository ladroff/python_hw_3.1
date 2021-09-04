y = {}
x = input()
for i in x:
    z = y.get(i)
    if z:
        y[i] = z + 1
    else:
        y[i] = 1
print(y)


