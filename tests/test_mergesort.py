import unittest
from src.mergesort.mergesort import merge_sort


class Test(unittest.TestCase):
    def setUp(self):
        self.unsortedList = [2, 5, 4, 7, 1, 8, 3, 9, 6, 0]
        self.sortedList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_shouldBeSorted(self):
        self.assertEqual(self.sortedList, merge_sort(self.unsortedList))
