from typing import List
from unittest import TestCase

from leetcode.find_pivot_index import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertEqual(self.pivotIndex([1, 7, 3, 6, 5, 6]), 3)

    def test_example2(self):
        self.assertEqual(self.pivotIndex([1, 2, 3]), -1)

    def test_example3(self):
        self.assertEqual(self.pivotIndex([2, 1, -1]), 0)

    def test_min_length(self):
        self.assertEqual(self.pivotIndex([2]), 0)

    def test_right(self):
        self.assertEqual(self.pivotIndex([1, 2, 3, -3, -2, -1, 100]), 6)

    def test_left(self):
        self.assertEqual(self.pivotIndex([100, 1, 2, 3, -3, -2, -1]), 0)

    def pivotIndex(self, nums: List[int]) -> int:
        sol = Solution()
        return sol.pivotIndex(nums)
