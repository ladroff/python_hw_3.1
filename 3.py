x = int(input("Введите год :"))
y, z, a = x % 4, x % 100, x % 400
if y == 0 and z != 0 or a == 0:
    print(x, "Этот год - высокосный")
else:
    print(x, "Этот год - не высокосный")



