n = int(input())
y = 1
if 4 < n < 16:
    for n in range(2, n + 1):
        y *= n
    print(y)
else:
    print("Введите верное число ")

