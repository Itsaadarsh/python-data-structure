# Linked List
# Simple linked list with 3 nodes

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
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":

    linklist = LinkedList()

    # Creating 3 Nodes
    # Initializing the first node to the linked list
    linklist.head = Node('First node')
    second = Node('Second node')
    third = Node('Third node')

    linklist.head.next = second  # Linking first node to second node
    second.next = third  # Linking second node to third node

    linklist.display()  # Displaying the data in the linked list
