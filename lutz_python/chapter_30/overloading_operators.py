import random

"""
МЕТОДЫ ПЕРЕГРУЗКИ ОПЕРАЦИЙ
(overloading operators)
примеры основных операций
! указаны не все контексты !
"""

# операция инициализации экземпляра
class TestClass:
    def __init__(self, value=None):
        self.value = value if value is not None else 0
        self.list = [random.randint(0, 100) for _ in range(self.value)]

    def __str__(self):
        return str(self.value)

# операция сложения
class TestAdd(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __add__(self, value):
        return TestAdd(self.value + value)

# операция вычитания
class TestSub(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __sub__(self, value):
        return TestSub(self.value - value)

# операция побитого или
class TestOr(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __or__(self, value):
        return TestOr(self.value | value)

# операция деструктуризации, уничтожения объекта
# связан с некоторыми трудностями, так как не очевидно как будет работать сборщик мусора
# Если в __del__ возникает исключение, оно будет проигнорировано, но появится предупреждение в stderr.
class TestDel(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __del__(self):
        print(f'{self.__class__.__name__} => Удаление объект')

# получение строкового представления
class TestRepr(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'returned: {self.value}'

# получение строкового представления (более специфичное чем repr, используется в print и str)
class TestStr(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'returned: {self.value}'

# вызов экземпляра, позволяет экземпляру вести себя как функция
class TestCall(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self, other):
        return self.value + other

# перехватывает обращение к атрибуту в том случае если в дереве наследования не найден указанны атрибут
class TestGetAttr(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = TestGetAttrData()

    def __getattr__(self, x):   # может послужить для делегирвания доступ к атрибутам другим объектам
        if x == 'age':
            return self.data.age
        if x == 'name':
            return self.data.name
        raise AttributeError(x)

class TestGetAttrData:
    age = 40
    name = "<NAME>"

# присваивание атрибуту класса значения
# важно, что напрямую присваивание в самом методе __setatrr__ вызовет рекурсию и последующую ошибку переполнения стека
# как выход - присвоить значение через атрибут __dict__
class TestSetAttr(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setattr__(self, attr, value):
        if attr in ('value', 'list'):
            self.__dict__[attr] = value
        else:
            raise AttributeError(f'{attr} is not a valid attribute')

# операция удаление атрибута
class TestDelAttr:
    def __init__(self):
        self.value = 10

    def __delattr__(self, attr):
        if attr in ('value', 'list'):
            del self.__dict__[attr]     # так же для избежания рекурсии, удаление происходит через __dict__
        else:
            raise AttributeError(f'{attr} is not a valid attribute')

class TestGetAttribute(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattribute__(self, other):
        cls_name = object.__getattribute__(self, '__class__').__name__
        print(f'{cls_name} => Попытка доступа к атрибуту: {other}')
        return super().__getattribute__(other)

# операции индексирования, в том числе нарезания (slice)
class TestGetItem(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getitem__(self, idx):
        # в случае, если метод вызывается нарезанием, то в аргумент приходит объект slice
        if isinstance(idx, int):
            if idx < len(self.list):
                return TestGetItem(value=self.list[idx])
            return TestGetItem()
        return idx

# операции индексирования, в том числе нарезания (slice)
class TestGetItemDict(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._dict = {str(random.randint(0, 100)): self.value for _ in range(self.value)}

    def __getitem__(self, idx):
        if isinstance(idx, int):
            idx = str(idx)

        if isinstance(idx, str):
            if idx in self._dict:
                return TestGetItemDict(value=self._dict[idx])
            return TestGetItemDict()
        return idx

# операции присваивания по индексу или ключу, в том числе нарезания (slice)
# например obj[1:3] = [10, 20]
class TestSetItem(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setitem__(self, idx, value):
        if isinstance(idx, int):
            self.list[idx] = value

    def __str__(self):
        return str(self.list)

# операция удаления по индексу
class TestDelItem(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list = [i for i in range(self.value)]

    def __delitem__(self, idx):
        del self.list[idx]

# операции булевского контекста
# сначала пытается полчить из __bool__, иначе пытается вывести значении
# истинности из длинны объекта
class TestBoolLen(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __len__(self):
        return 0

    def __bool__(self):
        return True


# аналогичные операции сравнения:
# lt gt
# le ge
# eq ne
# операции сравнения: >
class TestGt(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __gt__(self, other):
        return self.value > other

# операции сравнения: <
class TestLt(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __lt__(self, other):
        return self.value < other

# Операции правостороннего сложения. То есть когда класс стоит справа от оператора +
class TestRadd(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __radd__(self, other):
        return self.value + other

# Операция сложения на месте. Например: x += 2
class TestIadd(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __iadd__(self, other):
        return self.value + other

# операции в контексте итерации
class TestIter:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

# операция проверка членства in
# Если не определен этот метод, то используется __iter__, или если и его нет, то __getitem__
class TestContains:
    def __init__(self, value):
        self.value = value

    def __contains__(self, x):
        return x not in self.value

# Позволяет объекту вести себя как целое число в некоторых операциях, т.е. Возвращает целое число
# Например в индексации массивов или срезов, а так же в операциях bin hex и прочее
class TestIndex(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __index__(self) -> int:    # не принимает аргументы, возвращает int, иначе ошибка
        # если операция индексация,
        # используя этот объект в индекс будет падать 0, а значит первый элемент
        return 0

# пример перегрузки операции итерации с отдельным итератором и возможностью множественного прохода
class TestIteration:
    def __init__(self, arg):
        self.arg = arg
    def __iter__(self):
        return TestIterator(self.arg)

class TestIterator:
    def __init__(self, arg):
        self.arg = arg
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.arg):
            raise StopIteration
        item = self.arg[self.offset]
        self.offset += 1
        return item

# еще один пример использования __iter__ с оператором yield, который сам по себе уже генератор
# поддерживает множество активных итераторов
class TestIterYield:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):     # когда вызывается __iter__ он, возвращает новый генератор.
        for val in range(self.start, self.stop):
            yield val

def handler(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            print(f'{func.__name__} => {res}')

        except Exception as e:
            print(f'Error! {func.__name__} => {e}')

    return wrapper

@handler
def test_add():
    n = TestAdd(value=1)
    r = n + 2
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r.value}"

@handler
def test_sub():
    n = TestSub(value=1)
    r = n - 2
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r.value}"

@handler
def test_or():
    n = TestOr(value=1)
    r = n | 2
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r.value}"

def test_del():
    n = TestDel()
    del n

@handler
def test_repr():
    n = TestRepr(5)
    n = repr(n)
    return f"Operation returned instance of '{n.__class__.__name__}'. Value: {n}"

@handler
def test_str():
    n = TestStr(5)
    return f"Operation returned instance of '{n.__class__.__name__}'. Value: {n}"

@handler
def test_call():
    n = TestCall(5)
    r = n(2)
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_getattr():
    n = TestGetAttr(5)
    r = f'{n.name}: {n.age} and {n.value}'
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_setattr():
    n = TestSetAttr(5)
    n.value = 2
    return f"Operation returned instance of '{n.value.__class__.__name__}'. Value: {n.value}"

@handler
def test_delattr():
    n = TestDelAttr()
    del n.value
    return f"Operation returned instance of '{n.__dict__.__class__.__name__}'. Value: {n.__dict__}"

def test_getattribute():
    n = TestGetAttribute(5)

@handler
def test_getitem():
    n = TestGetItem(value=5)
    r = n[1]
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_getitem_2():
    n = TestGetItem(value=3)
    r = n[4]
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_getitem_3():
    n = TestGetItem(value=5)
    r = n[0:3:]
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_getitem_dict():
    n = TestGetItemDict(value=5)
    r = n[random.choice(list(n._dict.keys()))]
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_setitem():
    r = TestSetItem(value=5)
    r[3] = 'test'
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_delitem():
    n = TestDelItem(5)
    del n[3]
    return f"Operation returned instance of '{n.__class__.__name__}'. Value: {n.list}"

@handler
def test_len():
    n = TestBoolLen(5)
    r = len(n)
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_bool():
    n = TestBoolLen(5)
    r = bool(n)
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_gt():
    n = TestGt(5)
    r = n > 3
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_lt():
    n = TestLt(5)
    r = n < 3
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_radd():
    n = TestRadd(5)
    r = 2 + n
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_iadd():
    n = TestIadd(5)
    n += 2
    return f"Operation returned instance of '{n.__class__.__name__}'. Value: {n}"

@handler
def test_iter():
    n  = TestIter(0, 5)
    r = ''
    for i in n:     # в for попадает итератор, который на каждом проходе вызывает у него __next__
        r += f'{i} '
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_iter_multiply():
    n = TestIteration('abcd')   # создается объект
    r = []
    # for на каждом проходе вызывает у итератора метод __next__
    for i in n:                 # в цикл отдается новый итератор с новым состоянием
        for y in n:             # отдается еще один и тоже с новым состоянием
            r.append(f'{i}{y}')
    r = ' '.join(r)
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_iter_multiply_list():
    n = TestIteration(['a', 'b', 'c', 'd'])
    r = []
    for i in n:
        for y in n:
            r.append(f'{i}{y}')
    r = ' '.join(r)
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_iter_yield():
    n = TestIterYield(0, 5)
    r = []
    for i in n:
        for y in n:
            r.append(f'{i}{y}')
    r = ' '.join(r)
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"


@handler
def test_next():
    pass

@handler
def test_contains():
    n = TestContains('abcd')
    r = 'a' in n
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_index():
    n = TestIndex(5)
    r = n.list[n] # т.е. из списка проиндексировать и вернуть элемент по индексу, который вернул метод
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"


if __name__ == '__main__':
    test_add()
    test_sub()
    test_or()
    test_del()
    test_repr()
    test_str()
    test_call()
    test_getattr()
    test_setattr()
    test_delattr()
    test_getattribute()
    test_getitem()
    test_getitem_2()
    test_getitem_3()
    test_getitem_dict()
    test_setitem()
    test_delitem()
    test_len()
    test_bool()
    test_gt()
    test_lt()
    test_radd()
    test_iadd()
    test_iter()
    test_iter_multiply()
    test_iter_multiply_list()
    test_iter_yield()
    test_contains()
    test_index()
