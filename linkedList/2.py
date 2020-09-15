# Recursive display of Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self, node):

        if(node != None):
            print(node.data)  # Prints the linked list as it is. (EG : 5, 2, 9)
            self.display(node.next)  # RECURSION O(n) & No.of calls (n+!)

            self.display(node.next)  # RECURSION O(n) & No.of calls (n+!)
            print(node.data)  # Prints the reverserd linked list (EG : 9, 2, 5)
        else:
            return


if __name__ == "__main__":

    linklist = LinkedList()

    # Creating 3 Nodes
    # Initializing the first node to the linked list
    linklist.head = Node(5)
    second = Node(2)
    third = Node(9)

    linklist.head.next = second  # Linking first node to second node
    second.next = third  # Linking second node to third node

    # Displaying the data in the linked list recursively
    linklist.display(linklist.head)
