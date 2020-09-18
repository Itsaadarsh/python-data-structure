# Inserting n elements in a Linked List
# Both Looping and Recursion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self, node):
        # Looping Method
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

        # Recursive Method
        # if(node != None):
        #     print(node.data)  # Prints the linked list as it is. (EG : 5, 2, 9)
        #     self.display(node.next)  # RECURSION O(n) & No.of calls (n+!)

        #     # self.display(node.next)  # RECURSION O(n) & No.of calls (n+!)
        #     # print(node.data)  # Prints the reverserd linked list (EG : 9, 2, 5)
        # else:
        #     return


if __name__ == "__main__":

    n = int(input('Enter the No of element to be inserted: '))
    llist = LinkedList()

    d = {}
    for i in range(n):
        ele = (input(f'Enter the element for node {i+1} : '))
        d["node{}".format(i)] = Node(ele)

    llist.head = d['node0']
    for i in range(n-1):
        d['node{}'.format(i)].next = d['node{}'.format(i+1)]

    llist.display(llist.head)
