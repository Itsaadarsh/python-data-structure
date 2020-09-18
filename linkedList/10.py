# Creating n elements in a linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def creating(self):
        n = int(input('Enter the number of NODES : '))

        for i in range(n):
            data = input('Enter the data for NODE {} : '.format(i+1))
            self.pushingElements(data)


if __name__ == "__main__":

    llist = LinkedList()
    llist.creating()
    llist.display()
