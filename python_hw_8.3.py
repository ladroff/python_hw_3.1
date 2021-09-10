a = int(input("a="))
b = int(input("b="))
def kvadrat (a, b):
    for i in range(b):
        if not i or i == b - 1:
            print('*' * a, end =' ')
            print()
        else:
            print('*' + ' ' * (a - 2) + '*')
print(kvadrat(a, b))