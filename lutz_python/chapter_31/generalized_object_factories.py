def factory(aClass, *args, **kwargs):
    return aClass(*args, **kwargs)


class Spam:
    def doit(self, message):
        print(message)


class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job


if __name__ == '__main__':
    obj1 = factory(Spam)                                # Создать объект Spam
    obj2 = factory(Person, 'Arthur', 'King')      # Создать объект Person
    obj3 = factory(Person, name='Brian')