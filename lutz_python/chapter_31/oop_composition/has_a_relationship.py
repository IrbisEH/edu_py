"""
Object-Oriented Programming and Composition
Relationship: has-a
"""

from is_a_relationship import Server, PizzaRobot

class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, 'orders from', server)

    def pay(self, server):
        print(self.name, 'pays for item to', server)

class Oven:
    def bake(self):
        print('Oven bakes')

# получается что класс PizzaShop является контейнером и контроллером
class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)       # внедрение других объектов
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


if __name__ == '__main__':
    scene = PizzaShop()
    scene.order('Homer')
    print('...')
    scene.order('Marge')