import sys

class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data:
                break
            data = self.convertor(data)
            self.writer.write(data)

    def convertor(self, data):
        assert False, "not implemented"


class Uppercase(Processor):
    def convertor(self, data):
        return data.upper()


class Htmlize:
    def write(self, data):
        print('<PRE>%s</PRE>' % data.strip())


if __name__ == '__main__':
    reader = open('data.txt', 'r')
    writer = sys.stdout
    obj = Uppercase(reader, writer)
    obj.process()
    reader.close()

    print()

    reader = open('data.txt', 'r')
    writer = Htmlize()
    obj = Uppercase(reader, writer)
    obj.process()
    reader.close()

