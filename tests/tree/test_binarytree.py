import unittest
from src.tree.binarytree import BinaryTree


class Test(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree(50)

    def test_shouldInsertNode(self):
        self.tree.insert(40)

        result = self.tree.search(40)

        self.assertTrue(result)
