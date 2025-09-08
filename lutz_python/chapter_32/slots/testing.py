class A:
    pass


class B(A):
    __slots__ = ['a']


x = B()
x.a = 1
x.b = 2
print(x.__dict__)           # {'b': 2}
print(B.__dict__.keys())    # dict_keys(['__module__', '__slots__', 'a', '__doc__'])


class C:
    __slots__ = ['a']
    # a = 99        ValueError: 'a' in __slots__ conflicts with class variable
    b = 99