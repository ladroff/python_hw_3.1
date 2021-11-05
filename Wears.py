from Stuff import Stuff


class Wears(Stuff):

    def __init__(self, shoes, wears, balls, model, size, color, sex, wid):
        super().__init__(shoes, wears, balls)
        self.model = model
        self.size = size
        self.color = color
        self.sex = sex
        self.wid = wid

    def get_order(self):
        print("Order :")

    def __str__(self):
        return "Wears:" + super().__str__() + "size = {}, sex = {}, wid = {}".format(self.size, self.sex, self.wid)
