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

import timeit

base = """
Is = []
for i in range(1000):
    x = C()
    x.a = 1
    x.b = 2
    x.c = 3
    x.d = 4
    t = x.a + x.b + x.c + x.d
    Is.append(t)
"""

stmt_1 = """
class C():
    pass
""" + base


stmt_2 = """
class C():
    __slots__ = ['a', 'b', 'c', 'd']
""" + base

items = [('NonSlots', stmt_1), ('Slots', stmt_2)]

for title, stmt in items:
    print(f'{title} =>',  end=' ')
    print(min(timeit.repeat(stmt, number=1000, repeat=3)))



