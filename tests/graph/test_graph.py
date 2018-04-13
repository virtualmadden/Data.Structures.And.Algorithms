import unittest
from src.graph.graph import Graph


class Test(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(4)

    def test_shouldReturnGraph(self):
        self.graph.add_edge(0, 1)

        self.assertTrue(len(self.graph) is 1)
