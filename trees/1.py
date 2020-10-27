class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.key = data


def displayTree(temp):

    print(temp.key)
    print(temp.left.key)
    print(temp.left.left.key)
    print(temp.right.key)
    print(temp.right.right.key)


if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2)
    tree.left.left = Node(4)
    tree.right = Node(3)
    tree.right.right = Node(5)

    displayTree(tree)
