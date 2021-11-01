from Stuff import Stuff


class Shoes(Stuff):

    def __init__(self, shoes, wears, seawears, model, size, color, sex, price):
        super().__init__(shoes, wears, seawears)
        self.model = model
        self.size = size
        self.color = color
        self.sex = sex
        self.price = price

    def get_order(self):
        print("Order")

    def __str__(self):
        return "Shoes:" + super().__str__() + "size = {}, sex = {}, price = {}".format(self.size, self.sex, self.price)
