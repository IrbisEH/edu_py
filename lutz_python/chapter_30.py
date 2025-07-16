import inspect

""" Перегрузка операций """

# пример основных операций

# операция инициализации экземпляра
class TestClass:
    def __init__(self, start=None):
        self.data = start if start is not None else 0

# операция сложения
class TestAdd(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def __add__(self, other):
        return TestAdd(self.data + other)

# операция вычитания
class TestSub(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def __sub__(self, other):
        return TestSub(self.data - other)

# операция побитого или
class TestOr(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def __or__(self, other):
        return TestOr(self.data | other)

# операция деструктуризации, уничтожения объекта
class TestDel(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __del__(self, other):
        pass

# операция деструктуризации, уничтожения объекта
class TestRepr(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        pass

# операция деструктуризации, уничтожения объекта
class TestStr(TestClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        pass


    # # получение строкового представления
    # def __str__(self):
    #     return f'{self.__class__.__name__} instance {self.data} by str'
    # # позволяет экземпляру вести себя как функция
    # def __call__(self, *args, **kwargs):
    #     return f'args: {args} kwargs: {kwargs}'
    # # позволяет
    # def __getattr__(self, *args, **kwargs):
    #     pass
    # #
    # def __setattr__(self, *args, **kwargs):
    #     pass
    # #
    # def __delattr__(self, *args, **kwargs):
    #     pass
    # #
    # def __getattribute__(self, *args, **kwargs):
    #     pass
    # #
    # def __getitem__(self, *args, **kwargs):
    #     pass
    # #
    # def __delitem__(self, *args, **kwargs):
    #     pass
    # #
    # def __setitem__(self, *args, **kwargs):
    #     pass
    # #
    # def __len__(self, *args, **kwargs):
    #     pass
    # #
    # def __bool__(self):
    #     pass
    # #
    # def __lt__(self):
    #     pass
    # def __gt__(self):
    #     pass
    # def __le__(self):
    #     pass
    # def __ge__(self):
    #     pass
    # def __eq__(self):
    #     pass
    # def __ne__(self):
    #     pass
    # def __radd__(self):
    #     pass
    # def __iadd__(self):
    #     pass
    # def __iter__(self):
    #     pass
    # def __next__(self):
    #     pass
    # def __contains__(self):
    #     pass
    # def __index__(self):
    #     pass
    # def __enter__(self):
    #     pass
    # def __exit__(self):
    #     pass
    # def __get__(self):
    #     pass
    # def __set__(self):
    #     pass
    # def __delete__(self):
    #     pass
    # def __new__(self):
    #     pass


def test_add():
    n = TestAdd(5)
    res = n + 5
    print(f'result of {inspect.currentframe().f_code.co_name}: {res}')

def test_sub():
    n = CustomNumber(5)
    res = n - 2       # отдает новый экземпляр класса Number
    print(f'result of {inspect.currentframe().f_code.co_name}: {res}')

def test_or():
    n = CustomNumber(5)
    res = n | 2       # отдает новый экземпляр класса Number
    print(f'result of {inspect.currentframe().f_code.co_name}: {res}')

def test_del():
    n = CustomNumber(test_del=True)
    # по-хорошему надо перехватить вывод, пока результат должен быть на следующей строке
    print(f'result of {inspect.currentframe().f_code.co_name}:')
    del n

def test_repr():
    n = CustomNumber(5)
    res = repr(n)  # repr сам по себе не выводит ничего в консоль, но отдает строковое представление
    print(f'result of {inspect.currentframe().f_code.co_name}: {res}')

def test_str():
    n = CustomNumber(5)
    res = str(n)
    print(f'result of {inspect.currentframe().f_code.co_name}: {res}')

def test_call():
    n = CustomNumber(5)
    res = n(5, test='test')
    print(f'result of {inspect.currentframe().f_code.co_name}: {res}')

def test_getattr():
    n = CustomNumber(5)
    res = getattr(n, 'data')
    print(f'result of {inspect.currentframe().f_code.co_name}: {res}')


if __name__ == '__main__':
    # test_sub()
    # test_del()
    # test_or()
    # test_repr()
    # test_str()
    # test_call()
    # test_getattr()