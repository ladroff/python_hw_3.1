class Stuff:

    def __init__(self, shoes, wears, balls):
        self.shoes = shoes
        self.wears = wears
        self.balls = balls

    def get_order(self):
        pass

    def __str__(self):
        return "Shoes = {}, Wears = {}, Balls = {}".format(self.shoes, self.wears, self.balls)
