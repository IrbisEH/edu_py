import importlib

def tester(listerclass, sept=False):
    class Super:
        def __init__(self):
            self.data1 = 'spam'

        def ham(self):
            pass

    class Sub(Super, listerclass):
        def __init__(self):
            Super.__init__(self)


val = '357.5'

val = int(round(float(val)))

print(val)