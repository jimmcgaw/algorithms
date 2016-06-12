from maximum_subarray import max_subarray

import unittest

class MaximumSubarrayTest(unittest.TestCase):
    def setUp(self):
        self.array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    def test_returns_correct_subarray(self):
        total = max_subarray(self.array)
        self.assertEqual(total, 6)
