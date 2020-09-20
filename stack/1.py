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

    def poping(self):

        if(self.top == -1):
            print("STACK IS EMPTY")

        else:
            print('POPPED element is {}'.format(self.stack[self.top]))
            self.stack.pop()
            self.top -= 1
            print('Data Popped {}'.format(self.stack))

    def display(self):
        if(self.top == -1):
            print('STACK IS EMPTY')

        else:
            print('Elements in stack are..')
            for i in range(self.top):
                print('ELEMENT {} => {}'.format(i+1, self.stack[i]))

    def peak(self):

        if(self.top == -1):
            print('STACK IS EMPTY')

        else:
            print('Top Element in the stack is {}'.format(
                self.stack[self.top]))


if __name__ == "__main__":
    newStack = Stack()
    size = int(input('Enter the size of the stack : '))
    choice = '-1'
    while(choice != '4'):
        print("------------------------------------\n")
        print("    STACK IMPLEMENTATION PROGRAM    \n")
        print("------------------------------------\n")
        print("1. Push\n")
        print("2. Pop\n")
        print("3. Peek\n")
        print("4. Exit\n")
        print("5. Display Elements\n")
        print("------------------------------------\n")
        choice = (input("Enter your choice: "))

        if(choice == '1'):
            newStack.pushing(size)
        elif(choice == '2'):
            newStack.poping()
        elif(choice == '3'):
            newStack.peak()
        elif(choice == '4'):
            choice = '4'
        elif(choice == '5'):
            newStack.display()
        else:
            print('Invalid INPUT! Try again')
