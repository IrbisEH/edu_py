"""
МЕТОДЫ ПЕРЕГРУЗКИ ОПЕРАЦИЙ
(overloading operators)
примеры основных операций
"""

# операция инициализации экземпляра
class TestClass:
    def __init__(self, value=None):
        self.value = value if value is not None else 0

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

class TestGetAttr(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattr__(self):
        pass

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

class TestGetItem(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getitem__(self):
        pass

class TestDelItem(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __delitem__(self):
        pass

class TestSetItem(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setitem__(self):
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

class TestIter(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __iter__(self):
        pass

class TestNext(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __next__(self):
        pass

class TestContains(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __contains__(self):
        pass

class TestIndex(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __index__(self):
        pass

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


def handler(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            print(f'{func.__name__} => {res}')

        except Exception as e:
            print(f'{func.__name__} => {e}')

    return wrapper

@handler
def test_add():
    n = TestAdd(value=1)
    y = n + 2
    return f"Operation returned instance of '{y.__class__.__name__}'. Value: {y.value}"

@handler
def test_sub():
    n = TestSub(value=1)
    y = n - 2
    return f"Operation returned instance of '{y.__class__.__name__}'. Value: {y.value}"

@handler
def test_or():
    pass

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
    pass

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
    pass

@handler
def test_delitem():
    pass

@handler
def test_setitem():
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
    pass

@handler
def test_next():
    pass

@handler
def test_contains():
    pass

@handler
def test_index():
    pass

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
    # test_del()
    # test_or()
    # test_repr()
    # test_str()
    # test_call()
    # test_getattr()
    #test_setattr()
    #test_delattr()
    #test_getattribute()
    #test_getitem()
    #test_delitem()
    #test_setitem()
    #test_len()
    #test_bool()
    #test_lt()
    #test_gt()
    #test_ge()
    #test_eq()
    #test_ne()
    #test_radd()
    #test_iadd()
    #test_iter()
    #test_next()
    #test_contains()
    #test_index()
    #test_enter()
    #test_exit()
    #test_get()
    #test_set()
    #test_delete()
    #test_new()
