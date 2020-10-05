class Printer(object):
    def __init__(self, name="Cannon", printing_speed=25, price_in_uah=2500):
        self.name = name
        self.printing_speed = printing_speed
        self.price = price_in_uah

    @staticmethod
    def compare(first, second, tag="price", greater_than=True):
        if tag == "price":
            return greater_than and first.price > second.price
        else:
            return greater_than and first.printing_speed > second.printing_speed





