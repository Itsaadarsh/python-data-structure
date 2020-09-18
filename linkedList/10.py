# Deleting elements from a linked list
# Manually creating n elements and DELETING them at a given index


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

    def deletingAtBeginning(self):

        self.head = self.head.next
        self.display()

    def deletingAtEnd(self):
        temp = self.head
        while(temp.next.next):
            temp = temp.next
        temp.next = None

        if(temp):
            self.display()

    def deletingAnItem(self):
        item = input('Enter the item you want to delete : ')
        temp = self.head

        while(temp.next):
            if(temp.data == item):
                temp = temp.next
                self.head = temp
                break
            if(temp.next.data == item):
                temp.next = temp.next.next
                break
            temp = temp.next

        if(temp):
            self.display()

    def deletingAnIndex(self):
        index = int(input('Enter the index you want to delete : '))
        temp = self.head
        ind = 0
        while(temp.next):
            if(ind == index):
                temp = temp.next
                self.head = temp
                break
            ind += 1
            if(ind == index):
                temp.next = temp.next.next
                break
            temp = temp.next

        if(temp):
            self.display()


if __name__ == "__main__":

    llist = LinkedList()

    # Creating n elements
    llist.creating()

    # Deleting at the BEGINNING
    llist.deletingAtBeginning()

    # Deleting at the END
    llist.deletingAtEnd()

    # Deleting an item
    llist.deletingAnItem()

    # Deleting at an given index
    llist.deletingAnIndex()
