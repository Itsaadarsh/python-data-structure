# Sum of all elements in a Linked List
# Both Looping and Recursion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def displayCount(self, node):
        # Looping method
        # temp = self.head
        # totalSum = 0
        # while(temp):
        #     totalSum += temp.data
        #     temp = temp.next
        # return totalSum  # O(N)

        # Recursive method
        if(node != None):
            return self.displayCount(node.next) + node.data
        else:
            return 0


if __name__ == "__main__":

    llist = LinkedList()

    llist.head = Node(50)
    second = Node(20)
    third = Node(30)

    llist.head.next = second
    second.next = third

    print('Sum of all Elements =>', llist.displayCount(llist.head))
