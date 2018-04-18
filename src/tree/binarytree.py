class Node(object):
    def insert(self, value):
        if self.value > value and self.left is None:
            self.left = Node(value)

            return True
        elif self.value < value and self.right is None:
            self.right = Node(value)

            return True
        else:
            if self.value > value:
                return self.left.insert(value)
            elif self.value < value:
                return self.right.insert(value)

    def search(self, value):
        if self.value is value:
            return True
        elif self.value > value and self.left is not None:
            return self.left.search(value)
        elif self.value < value and self.right is not None:
            return self.right.search(value)
        else:
            return False

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree(object):
    def insert(self, value):
        if self.root.search(value):
            return False

        return self.root.insert(value)

    def search(self, value):
        return self.root.search(value)

    def __init__(self, value=0):
        self.root = Node(value)
