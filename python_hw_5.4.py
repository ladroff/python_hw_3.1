b = int(input())
a = int(input())
print("*" * a)
for i in range(b - 2):
    print("*", ' ' * (a - 2), "*", sep='')
print("*" * a)