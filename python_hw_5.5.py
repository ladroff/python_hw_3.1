x = input()
y = 0
z = 0
for i in x:
    if int(i) % 2 == 0:
        y += 1
    else:
        z += 1
print("Четных:", y, "Нечетных:", z)