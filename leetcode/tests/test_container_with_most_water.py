from typing import List
from unittest import TestCase

from leetcode.container_with_most_water import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertEqual(self.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_example2(self):
        self.assertEqual(self.maxArea([1, 1]), 1)

    def test_zeroes(self):
        self.assertEqual(self.maxArea([0, 0, 0, 0, 0, 0, 0]), 0)

    def maxArea(self, height: List[int]) -> int:
        sol = Solution()
        return sol.maxArea(height)
