x = int(input("x"))
y = int(input("y"))
z = int(input("z"))
if x > y and x > z:
    print(x,"Больше всех")
if y > x and y > z:
    print(y,"Больше всех")
else:
    print(z,"Больше всех")
if x == y or y == z or x == z:
    print("Числа должны быть разными!")