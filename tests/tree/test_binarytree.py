import unittest
from src.tree.binarytree import BinaryTree


class Test(unittest.TestCase):
    def test_shouldInsertNode(self):
        tree = BinaryTree(4)

        self.assertTrue(tree.root.value is 4)
        self.assertTrue(tree.root.left is None)
        self.assertTrue(tree.root.right is None)
