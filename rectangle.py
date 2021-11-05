import numbers


class Rectangle:

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = self.x * self.y

    def __str__(self):
        return "Rectangle [x = {}, y = {}]".format(self.x, self.y)

    def __eq__(self, other):
        if self.x * self.y == other.x * other.y:
            print("Площадь прямоугольников равна!")
        return self.x * self.y == other.x * other.y

    def __gt__(self, other):
        if self.x * self.y > other.x * other.y:
            print("Площадь первого прямоугольника больше!")
        else:
            print("Площадь второго прямоугольника больше!")

        return self.x * self.y > other.x * other.y

    def __add__(self, other):
        return self.x * self.y + other.x * other.y

    def __mul__(self, other):
        n = float(input("n ="))
        return self.x * self.y * n








