class Node(object):
    def insert(self, value):
        if self.left is None:
            self.left = Node(value)
        elif self.right is None:
            self.right = Node(value)
        else:
            self.left.insert(value)

    def search(self, value):
        if self.value is value:
            return True
        elif self.value > value:
            return self.left.search(value)
        elif self.value < value:
            return self.right.search(value)
        else:
            return False

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree(object):
    def insert(self, value):
        self.root.insert(value)

    def search(self, value):
        return self.root.search(value)

    def __init__(self, value=0):
        self.root = Node(value)
