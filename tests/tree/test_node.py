import unittest
from src.tree.node import Node


class Test(unittest.TestCase):
    def test_shouldInsertNode(self):
        node = Node(4)

        self.assertTrue(node.value is 4)
        self.assertTrue(node.left is None)
        self.assertTrue(node.right is None)
