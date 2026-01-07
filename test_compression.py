import unittest
from compression_function import *

class TestCompressNumbers(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(compress_numbers([1, 1, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(compress_numbers([0, 0, 1, 1, 0]), [0, 1, 0])

    def test_empty(self):
        self.assertEqual(compress_numbers([]), [])

    def test_single_element(self):
        self.assertEqual(compress_numbers([5]), [5])

    def test_no_duplicates(self):
        self.assertEqual(compress_numbers([1, 2, 3]), [1, 2, 3])

    def test_all_duplicates(self):
        self.assertEqual(compress_numbers([2, 2, 2, 2]), [2])

    def test_alternate_duplicates(self):
        self.assertEqual(compress_numbers([1, 1, 2, 1, 1, 3, 3]), [1, 2, 1, 3])

if __name__ == "__main__":
    unittest.main()