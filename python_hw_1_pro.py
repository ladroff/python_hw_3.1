class Shoes:
    def __init__(self, model, size, color, sex, price):
        self.model = model
        self.size = size
        self.color = color
        self.sex = sex
        self.price = price

class Client:
    def __init__(self, name, surname, sex, size, contact, email):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.size = size
        self.contact = contact
        self.email = email

class Orfer:
    def __init__(self, Client, Shoes, ):
        def order(self):
            print("Order")
        def __str__(self):
            return "Shoes [model = {}, size = {}, color =
            {}, sex = {}, price = {}]".format(self.model, self.size, self.color, self.sex, self.price)

            def client():
                print("Client")