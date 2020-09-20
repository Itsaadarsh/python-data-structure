# Stack Implementation using LinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def display(self):

        temp = self.top
        print('\nElements in the linkedlist STACK are...')
        while(temp):
            print(temp.data, "=>", end=" ")
            temp = temp.next
        return

    def pushing(self):
        data = input('Enter DATA : ')
        if(self.top is None):
            self.top = Node(data)
            print('DATA PUSHED')
        else:
            newNode = Node(data)
            newNode.next = self.top
            self.top = newNode
            print('DATA PUSHED')

    def popping(self):
        if(self.top is None):
            print('STACK IS EMPTY')
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            print('\n\nDATA POPPED')

    def peak(self):
        if(self.top is None):
            print('STACK IS EMPTY')

        else:
            print("\n\nTOP element in the stack is {}".format(self.top.data))


if __name__ == "__main__":

    newStack = Stack()
    choice = '-1'
    while(choice != '4'):
        print("\n\n------------------------------------\n")
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
            newStack.pushing()
        elif(choice == '2'):
            newStack.popping()
        elif(choice == '3'):
            newStack.peak()
        elif(choice == '4'):
            choice = '4'
        elif(choice == '5'):
            newStack.display()
        else:
            print('Invalid INPUT! Try again')
