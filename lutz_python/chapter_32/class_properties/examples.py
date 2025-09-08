def banner(func):
    def wrapper(*args, **kwargs):
        print(f"{'-' * 50} {func.__name__} {'-' * 50}")
        return func(*args, **kwargs)
    return wrapper

@banner
def example_1():
    class Operators:
        def __getattr__(self, name):
            if name == 'age':
                return 40
            else:
                raise AttributeError(name)

    x = Operators()

    print(x.age)
    # print(x.name)       # AttributeError: name

@banner
def example_2():
    class Properties:
        def get_age(self):
            return 40

        age = property(get_age, None, None, "Age property")

    x = Properties()

    print(x.age)

@banner
def example_3():
    class Properties:
        def getage(self):
            return 40
        def setage(self, value):
            print(f'set age to {value}')
            self._age = value
        age = property(getage, setage, None, "Age property")

    x = Properties()

    print(x.age)

    x.age = 50
    print(x._age)

    print(x.age)

    x.name = 'Bob'
    print(x.name)


if __name__ == '__main__':
    example_1()
    example_2()
    example_3()