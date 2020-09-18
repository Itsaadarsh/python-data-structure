# Searching element in a linkedlist

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

    def searching(self, item):
        temp = self.head
        ind = -1
        while(temp):
            ind += 1
            if(temp.data == item):
                print('ITEM FOUND AT INDEX {}'.format(ind))
                break
            temp = temp.next

        if(temp is None):
            print('ITEM NOT FOUND')


if __name__ == "__main__":

    llist = LinkedList()

    # Creating default nodes with data
    llist.pushingElements(5)
    llist.pushingElements(4)
    llist.pushingElements(3)
    llist.pushingElements(2)

    # Searching for element
    llist.searching(3)
