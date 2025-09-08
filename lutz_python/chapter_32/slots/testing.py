class C:
    __slots__ = ['a']
    # a = 99        ValueError: 'a' in __slots__ conflicts with class variable
    b = 99