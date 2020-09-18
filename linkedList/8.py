# Creating n elements in a linkedlist
# Manually creating n elements and inserting them at a given index

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


if __name__ == "__main__":

    llist = LinkedList()

    # Creating n elements
    llist.creating()

    # Displaying those n elements
    llist.display()

    # Inserting an element at a given index
    llist.insertingAtAIndex()
