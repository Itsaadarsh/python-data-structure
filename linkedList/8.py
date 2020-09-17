# Inserting elements in a Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self, node, newEle):
        # Looping Method
        temp = self.head
        while(temp):
            temp = temp.next
            print(temp.data)
        return temp


if __name__ == "__main__":

    n = int(input('Enter the No of element to be inserted: '))
    llist = LinkedList()

    d = {}
    for i in range(n):
        ele = (input(f'\nEnter the element for node {i+1} : '))
        d["node{}".format(i)] = Node(ele)

    llist.head = d['node0']

    newEle = input('\nEnter the new element : ')
    d["node{}".format(n)] = Node(newEle)
    d["node{}".format(n)].next = llist.head
    llist.head = d["node{}".format(n)]

    for i in range(n-1):
        d['node{}'.format(i)].next = d['node{}'.format(i+1)]

    # print('\nAfter Inserting =>', llist.display(llist.head))
    llist.display(llist.head)
