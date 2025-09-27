import unittest
from bubbleSort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(bubble_sort([5, 2, 9, 1]), [1, 2, 5, 9])
    def test_empty(self):
        self.assertEqual(bubble_sort([]), [])
    def test_sorted(self):
        self.assertEqual(bubble_sort([1, 2, 3]), [1, 2, 3])
    def test_reverse(self):
        self.assertEqual(bubble_sort([3, 2, 1]), [1, 2, 3])
    def test_duplicates(self):
        self.assertEqual(bubble_sort([2, 3, 2, 1]), [1, 2, 2, 3])

if __name__ == "__main__":
    unittest.main()
