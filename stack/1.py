# Stack implementation using array

class Stack:
    def __init__(self, size):
        self.stack = [None]*size
        self.top = -1
        self.size = size

    def pushing(self, size):

        if(self.top == size - 1):
            print("STACK OVERFLOW")

        else:
            while(self.top != self.size-1):
                data = input(
                    "Enter your {} data to PUSH into the stack :".format(self.top + 1))
                self.top += 1
                self.stack[self.top] = data
                print('Data Added')

    def poping(self):

        if(self.top == -1):
            print("STACK IS EMPTY")

        else:
            print('Data Popped {}'.format(self.stack[self.top]))
            self.top -= 1

    def display(self):
        if(self.top == -1):
            print('STACK IS EMPTY')

        else:
            print('Elements in stack are..')
            for i in range(self.top+1):
                print('ELEMENT {} => {}'.format(i+1, self.stack[i]))

    def peak(self):

        if(self.top == -1):
            print('STACK IS EMPTY')

        else:
            print('Top Element in the stack is {}'.format(
                self.stack[self.top]))


if __name__ == "__main__":
    size = int(input('Enter the size of the stack : '))
    newStack = Stack(size)
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
