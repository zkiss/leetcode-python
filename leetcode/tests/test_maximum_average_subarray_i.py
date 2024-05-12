from typing import List
from unittest import TestCase

from leetcode.maximum_average_subarray_i import Solution


class TestSolution(TestCase):
    def test_example1(self):
        result = self.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4)
        self.assertEqual(result, 12.75)

    def test_example2(self):
        result = self.findMaxAverage(nums=[5], k=1)
        self.assertEqual(result, 5)

    def test_all(self):
        result = self.findMaxAverage(nums=[1, 2, 3, 4, 5, 6], k=6)
        self.assertEqual(result, 3.5)

    def test_min(self):
        result = self.findMaxAverage([1, 2, 100, 3, 4, 5], 1)
        self.assertEqual(result, 100)

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sol = Solution()
        return sol.findMaxAverage(nums, k)
