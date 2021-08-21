x = int(input("Введите номер квартиры :"))
if x > 144 or x < 1:
    print("Такой квартиры не существует в этом доме!")
if x > 0 and x < 37:
    print("Квартира находится в 1 подъезде")
if x > 35 and x < 73:
    print("Квартира находится в 2 подъезде")
if x > 72 and x < 109:
    print("Квартира находится в 3 подъезде")
if x > 107 and x < 145:
    print("Квартира находится в 4 подъезде")
if x > 0 and x < 5 or x > 36 and x < 41 or x > 72 and x < 77 or x > 108 and x < 113:
    print("на первом этаже")
if x > 4 and x < 9 or x > 40 and x < 45 or x > 76 and x < 81 or x > 112 and x < 117:
    print("на втором этаже")
if x > 8 and x < 13 or x > 44 and x < 49 or x > 80 and x < 85 or x > 116 and x < 121:
    print("на третьем этаже")
if x > 12 and x < 17 or x > 48 and x < 53 or x > 84 and x < 89 or x > 120 and x < 125:
    print("на четвертом этаже")
if x > 16 and x < 21 or x > 52 and x < 57 or x > 88 and x < 93 or x > 124 and x < 129:
    print("на пятом этаже")
if x > 20 and x < 25 or x > 56 and x < 59 or x > 92 and x < 97 or x > 128 and x < 133:
    print("на шестом этаже")
if x > 24 and x < 29 or x > 60 and x < 65 or x > 96 and x < 101 or x > 132 and x < 137:
    print("на седьмом этаже")
if x > 28 and x < 33 or x > 64 and x < 69 or x > 100 and x < 105 or x > 136 and x < 141:
    print("на восьмом этаже")
if x > 32 and x < 37 or x > 68 and x < 73 or x > 104 and x < 109 or x > 140 and x > 145:
    print("на девятом этаже")