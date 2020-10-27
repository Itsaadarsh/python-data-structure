class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.key = data


def displayTree(temp):

    if (not temp):
        return

    displayTree(temp.left)
    print(temp.key, end=" ")
    displayTree(temp.right)


if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2)
    tree.left.left = Node(4)
    tree.right = Node(3)
    tree.right.right = Node(5)

    displayTree(tree)
