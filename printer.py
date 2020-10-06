class Printer(object):
    def __init__(self, name="Cannon", printing_speed=25, price_in_uah=2500):
        self.name = name
        self.printing_speed = printing_speed
        self.price = price_in_uah

    def __str__(self):
        return self.name + "; speed: " + str(self.printing_speed) + "; price: " + str(self.price)

    @staticmethod
    def compare(first, second, tag="price", greater_than=True):
        if tag == "price":
            return first.price > second.price
        else:
            return first.printing_speed > second.printing_speed





