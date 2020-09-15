# Searching elements in a Linked List
# Both Looping and Recursion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self, node, key):
        # Looping Method
        # temp = self.head
        # ind = 0
        # while(temp):
        #     ind += 1
        #     if(temp.data == key):
        #         return ind - 1
        #     temp = temp.next
        # return 'NOT FOUND'

        # Recursive Method
        if(node != None):
            ind = 0
            if(node.data == key):
                return ind
            ind = +1
            return(self.display(node.next, key))
        else:
            return 0


if __name__ == "__main__":

    n = int(input('Enter the No of element to be inserted: '))
    llist = LinkedList()

    d = {}
    for i in range(n):
        ele = (input(f'\nEnter the element for node {i+1} : '))
        d["node{}".format(i)] = Node(ele)

    key = (input('\nEnter the element to be found : '))
    llist.head = d['node0']
    for i in range(n-1):
        d['node{}'.format(i)].next = d['node{}'.format(i+1)]

    print('\nElement found index =>', llist.display(llist.head, key))
