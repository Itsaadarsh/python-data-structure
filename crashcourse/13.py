# CLASSES & OBJECTS

class number():
    def __init__(self, num):
        self.cNum = num

    def op(self, x):
        print(x)


n = number(10)
n.op(n.cNum)
