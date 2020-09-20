# Stack implementation using array

class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def pushing(self, size):

        if(self.top == size - 1):
            print("STACK OVERFLOW")

        else:
            for i in range(size):
                data = input(
                    "Enter your {} data to PUSH into the stack :".format(i+1))
                self.stack.append(data)
                self.top += 1
                print('Data Added {}'.format(self.stack))
