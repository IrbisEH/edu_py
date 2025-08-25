class Mylist(list):
    def __getitem__(self, offset):
        print('(indexing %s as %s)' % (self, offset))
        return list.__getitem__(self, offset - 1)


if __name__ == '__main__':
    l = list('abc')
    my_l = Mylist('abc')

    print(l)
    print(my_l)
    print(my_l[1])
    print(my_l[3])

    my_l.append('spam')
    print(my_l)
    my_l.reverse()
    print(my_l)