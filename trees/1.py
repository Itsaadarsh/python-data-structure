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


def insert(parent, data):

    if(parent is None):
        return Node(data)

    else:
        if(parent.key == data):
            return parent
        elif(parent.key < data):
            parent.right = insert(parent.right, data)
        else:
            parent.left = insert(parent.left, data)
    return parent


if __name__ == "__main__":
    tree = Node(3)
    insert(tree, 1)
    insert(tree, 2)
    insert(tree, 4)
    insert(tree, 0)
    displayTree(tree)
