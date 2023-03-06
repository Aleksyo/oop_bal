# здесь пишите программу
class Cart:
    def __init__(self):
        self.goods = []

    def add(self, *gd):
        for el in gd:
            self.goods.append(el)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        return [f"{el.name}: {el.price}" for el in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV('Sony', 100), TV('Samsung', 90), Table('Кухонный', 25), Notebook('Mac Air', 120), Notebook('Mac Pro', 150),
         Cup('Кружка', 5))
