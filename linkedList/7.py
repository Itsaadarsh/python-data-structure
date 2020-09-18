# Inserting elements into a linkedlist
# And creating node's data by default (Node('data'))


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

    def insertingBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertingEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def insertingAfterAnItem(self, item, data):
        temp = self.head
        while (temp):
            if(temp.data == item):
                newNode = Node(data)
                newNode.next = temp.next
                temp.next = newNode
                break
            temp = temp.next

        if(temp is None):
            print('Item {} Not found!'.format(item))
        else:
            self.display()

    def insertingBeforeAnItem(self, item, data):
        temp = self.head

        while(temp):
            if(temp.data == item):
                newNode = Node(data)
                newNode.next = temp
                temp = newNode
                self.head = temp
                break

            elif(temp.next is None):
                print('Item {} Not found!'.format(item))

            elif(temp.next.data == item):
                newNode = Node(data)
                newNode.next = temp.next
                temp.next = newNode
                break

            temp = temp.next

        if(temp):
            self.display()


if __name__ == "__main__":

    llist = LinkedList()
    llist.insertingEnd(0)
    llist.insertingEnd(1)
    llist.insertingEnd(2)
    llist.insertingEnd(3)
    llist.insertingAfterAnItem(3, 'AFTER')
    llist.insertingBeforeAnItem(3, 'BEFORE')
