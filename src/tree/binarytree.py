from .node import Node


class BinaryTree(object):
    def insert(self, value):
        if self.root.left is None:
            self.root.left = value
        elif self.root.right is None:
            self.root.right = value
        else:
            self.insert(self.root.left, value)

    def __init__(self, value=0):
        self.root = Node(value)
