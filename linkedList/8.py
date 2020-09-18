# Inserting elements in a Linked List
# And saving nodes into an OBJECT (d{})

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self, node):

        temp = self.head
        while(temp):
            print('\n', temp.data)
            temp = temp.next


if __name__ == "__main__":

    n = int(input('Enter the No of element to be inserted: '))
    llist = LinkedList()

    d = {}
    for i in range(n):
        ele = (input(f'\nEnter the element for node {i+1} : '))
        d["node{}".format(i)] = Node(ele)
# ---------------------------------------------------------------------------

    # Inserting at the BEGINNING of the linked list
    # llist.head = d['node0']

    # Linking new node with the first node

    # newEle = input('\nEnter the new element : ')
    # d["node{}".format(n)] = Node(newEle)
    # d["node{}".format(n)].next = llist.head
    # llist.head = d["node{}".format(n)]

    # for i in range(n-1):
    #     d['node{}'.format(i)].next = d['node{}'.format(i+1)]

# ---------------------------------------------------------------------------
    # # Inserting at the END of the linked list
    # llist.head = d['node0']

    # newEle = input('\nEnter the new element : ')
    # d["node{}".format(n)] = Node(newEle)

    # # Linking new node with the LAST node
    # for i in range(n):
    #     d['node{}'.format(i)].next = d['node{}'.format(i+1)]

    # print('\nAfter Inserting =>', llist.display(llist.head))

# ---------------------------------------------------------------------------

    # Inserting at a given index of the linked list

    llist.head = d['node0']

    newEle = input('\nEnter the new element : ')
    d["node{}".format(n)] = Node(newEle)

    index = int(input("Enter the index of the new number to be inserted : "))

    if(index == 0):
        d["node{}".format(n)].next = llist.head
        llist.head = d["node{}".format(n)]
        for i in range(n-1):
            d['node{}'.format(i)].next = d['node{}'.format(i+1)]
        llist.display(llist.head)

    elif(index == n):
        for i in range(n):
            d['node{}'.format(i)].next = d['node{}'.format(i+1)]
        llist.display(llist.head)

    else:
        for i in range(n-1):
            d['node{}'.format(i)].next = d['node{}'.format(i+1)]

        d["node{}".format(index-1)].next = d["node{}".format(n)]
        d["node{}".format(n)].next = d["node{}".format(index)]
        llist.display(llist.head)
# ---------------------------------------------------------------------------
