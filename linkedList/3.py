# Counting the number of nodes in a Linked List
# Both Looping and Recursive Method

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def displayCount(self, node):
        # Looping method
        temp = self.head
        tracker = 0
        while(temp):
            tracker += 1
            temp = temp.next
        return tracker  # O(N)

        # Recursive method
        # if(node != None):
        #     return self.displayCount(node.next) + 1
        # else:
        #     return 0


if __name__ == "__main__":

    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    print('Number of Nodes =>', llist.displayCount(llist.head))
