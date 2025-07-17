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
class TestDel(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __del__(self, other):
        pass

# получение строкового представления
class TestRepr(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        pass

# получение строкового представления
class TestStr(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        pass

# вызов экземпляра, позволяет экземпляру вести себя как функция
class TestCall(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self):
        pass

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

class TestSetAttr(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setattr__(self):
        pass

class TestDelAttr(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __delattr__(self):
        pass

class TestGetAttribute(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattribute__(self):
        pass

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

class TestDelItem(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __delitem__(self):
        pass

class TestLen(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __len__(self):
        pass

class TestBool(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __bool__(self):
        pass

class TestLt(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __lt__(self):
        pass

class TestGt(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __gt__(self):
        pass

class TestLe(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __le__(self):
        pass

class TestGe(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __ge__(self):
        pass

class TestEq(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __eq__(self):
        pass

class TestNe(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __ne__(self):
        pass

class TestRadd(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __radd__(self):
        pass

class TestIadd(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __iadd__(self):
        pass

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

class TestEnter(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __enter__(self):
        pass

class TestExit(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __exit__(self):
        pass

class TestGet(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __get__(self):
        pass

class TestSet(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __set__(self):
        pass

class TestDelete(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __delete__(self):
        pass

class TestNew(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __new__(self):
        pass

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

@handler
def test_del():
    pass

@handler
def test_repr():
    pass

@handler
def test_str():
    pass

@handler
def test_call():
    pass

@handler
def test_getattr():
    n = TestGetAttr(5)
    r = f'{n.name}: {n.age} and {n.value}'
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_getattr_error():
    n = TestGetAttr(5)
    r = n.someattr
    return f"Operation returned instance of '{r.__class__.__name__}'. Value: {r}"

@handler
def test_setattr():
    pass

@handler
def test_delattr():
    pass

@handler
def test_getattribute():
    pass

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
    pass

@handler
def test_len():
    pass

@handler
def test_bool():
    pass

@handler
def test_lt():
    pass

@handler
def test_gt():
    pass

@handler
def test_ge():
    pass

@handler
def test_eq():
    pass

@handler
def test_ne():
    pass

@handler
def test_radd():
    pass

@handler
def test_iadd():
    pass

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

@handler
def test_enter():
    pass

@handler
def test_exit():
    pass

@handler
def test_get():
    pass

@handler
def test_set():
    pass

@handler
def test_delete():
    pass

@handler
def test_new():
    pass


if __name__ == '__main__':
    test_add()
    test_sub()
    test_or()
    # test_del()
    # test_repr()
    # test_str()
    # test_call()
    test_getattr()
    test_getattr_error()
    #test_setattr()
    #test_delattr()
    #test_getattribute()
    test_getitem()
    test_getitem_2()
    test_getitem_3()
    test_getitem_dict()
    test_setitem()
    #test_delitem()
    #test_len()
    #test_bool()
    #test_lt()
    #test_gt()
    #test_ge()
    #test_eq()
    #test_ne()
    #test_radd()
    #test_iadd()
    test_iter()
    test_iter_multiply()
    test_iter_multiply_list()
    test_iter_yield()
    test_contains()
    test_index()
    #test_enter()
    #test_exit()
    #test_get()
    #test_set()
    #test_delete()
    #test_new()
