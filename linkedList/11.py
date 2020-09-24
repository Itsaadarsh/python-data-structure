# Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):

        temp = self.head
        while(temp):
            print('\n', temp.data)
            temp = temp.next

    def pushingElements(self, data):
        newNode = Node(data)
        newNode.next = None
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp

    def creating(self):
        n = int(input('Enter the number of NODES : '))

        for i in range(n):
            data = input('Enter the data for NODE {} : '.format(i+1))
            self.pushingElements(data)

    def insertingAtAIndex(self):

        data = input('Enter the data for NEWNODE : ')
        index = int(input('Enter the index : '))
        temp = self.head
        ind = 0
        while(temp):
            if(ind == index):
                newNode = Node(data)
                newNode.next = temp
                temp = newNode
                self.head = temp
                break
            ind += 1
            if (ind == index):
                newNode = Node(data)
                newNode.next = temp.next
                temp.next = newNode
                break
            temp = temp.next

        if(temp is None):
            print('Item Not found at index {}!'.format(index))
        else:
            self.display()

    def insertAtBeginning(self):
        data = input('Enter the data for NEWNODE : ')
        newNode = Node(data)
        newNode.next = self.head
        newNode.prev = None
        if self.head:
            self.head.prev = newNode
        self.head = newNode

    def insertAfter(self, afterData):
        data = input('Enter the data for NEWNODE : ')
        temp = self.head
        while(temp):
            if(temp.data == afterData):
                newNode = Node(data)
                newNode.next = temp.next
                newNode.prev = temp
                temp.next = newNode
                temp.next.prev = newNode
            temp = temp.next


if __name__ == "__main__":

    llist = LinkedList()

    # Creating n elements
    llist.creating()

    # Displaying those n elements

    # Inserting an element at a given index
    # llist.insertingAtAIndex()

    # llist.insertAtBeginning()
    # llist.insertAfter('2')
    llist.display()
