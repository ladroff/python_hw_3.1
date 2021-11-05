import numbers


class CorrectFractions:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        if self.x < self.y < 1:
            print('Дробь - "правильная".')
        else:
            print('Дробь - "не правильная".')

    def __str__(self):
        return "CorrectFractions [x = {}, y = {}]".format(self.x, self.y)

    def __eq__(self, other):
        if self.x / self.y == other.x / other.y:
            print("Дроби равны.")
        return self.x * self.y == other.x * other.y

    def __lt__(self, other):
        if (self.x / self.y) < (self.x / self.y):
            print("Первая дробь больше.")
        else:
            print("Вторая дробь больше.")
        return (self.x / self.y) < (other.x / other.y)

    def __add__(self, other):
        return (self.x + other.x) / (self.y + other.y)

    def __sub__(self, other):
        return self.x / self.y - other.x / other.y

    def __mul__(self, other):
        return (self.x * other.x) / (self.y * other.y)
