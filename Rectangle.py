
class Rectangle:
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length':self.length}
        yield {'width':self.width}

rec = Rectangle(5,10)

for i in rec:
    print(i)
