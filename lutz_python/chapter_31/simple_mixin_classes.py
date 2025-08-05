# MRO (Method Resolution Order) example
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass


# example 2
class ListInstance:
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__,
            id(self),
            self.__attrnames())


class Spam(ListInstance):
    def __init__(self):
        self.data1 = 'food'


class Super:
    def __init__(self):
        self.data1 = 'spam'

    def ham(self):
        pass


class Sub(Super, ListInstance):
    def __init__(self):
        Super.__init__(self)
        self.data2 = 'eggs'
        self.data3 = 42

    def spam(self):
        pass


if __name__ == '__main__':
    # MRO example
    # print(D.__mro__)        # атрибут класса! а не экземпляра

    # example2
    x = Spam()
    print(x)

    # real mixin classes
    x = Sub()
    print(x)
