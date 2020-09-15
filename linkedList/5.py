# Greatest element in a Linked List
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
        temp = self.head
        maxEle = -1
        while(temp):
            if(temp.data > maxEle):
                maxEle = temp.data
            elif(temp.data == maxEle):
                maxEle = temp.data
            else:
                maxEle = maxEle
            temp = temp.next
        return maxEle  # O(N)

        # Recursive method
        # maxEle = -1
        # if(node != None):
        #     maxEle = self.displayCount(node.next)
        #     if(maxEle > node.data):
        #         return maxEle
        #     else:
        #         return node.data
        # else:
        #     return 0


if __name__ == "__main__":

    llist = LinkedList()

    llist.head = Node(10)
    second = Node(-2)
    third = Node(20)

    llist.head.next = second
    second.next = third

    print('Greatest element =>', llist.displayCount(llist.head))
