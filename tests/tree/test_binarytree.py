import unittest
from src.tree.binarytree import BinaryTree


class Test(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree(50)

    def test_shouldInsertNode(self):
        self.assertTrue(self.tree.insert(40))

    def test_shouldNotInsertSameNode(self):
        self.tree.insert(40)

        self.assertFalse(self.tree.insert(40))

    def test_shouldNotInsertSameNode(self):
        self.tree.insert(40)
        self.tree.insert(60)

        self.assertTrue(self.tree.root.right is not None and self.tree.root.left is not None)
