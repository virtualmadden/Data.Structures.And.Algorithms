import unittest
from src.tree.binarytree import BinaryTree


class Test(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree(50)

    def test_shouldInsertNode(self):
        self.assertTrue(self.tree.insert(40))
