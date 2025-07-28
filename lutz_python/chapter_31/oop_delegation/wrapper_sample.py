class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, name):
        print('Trace: ' + name)
        return getattr(self.wrapped, name)

    def __str__(self):
        return str(self.wrapped)

if __name__ == '__main__':
    x = Wrapper([1, 2, 3, 4, 5])
    x.append(6)
    print(x)