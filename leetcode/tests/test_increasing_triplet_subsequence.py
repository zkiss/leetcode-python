from typing import List
from unittest import TestCase

from leetcode.increasing_triplet_subsequence import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertTrue(self.increasingTriplet([1, 2, 3, 4, 5]))

    def test_example2(self):
        self.assertFalse(self.increasingTriplet([5, 4, 3, 2, 1]))

    def test_example3(self):
        self.assertTrue(self.increasingTriplet([2, 1, 5, 0, 4, 6]))

    def test_min(self):
        self.assertFalse(self.increasingTriplet([0]))
        self.assertFalse(self.increasingTriplet([0, 1]))
        self.assertFalse(self.increasingTriplet([0, 2, 1]))
        self.assertTrue(self.increasingTriplet([0, 1, 2]))

    def test_sames(self):
        self.assertFalse(self.increasingTriplet([1, 1, 1, 1, 1, 1]))

    def increasingTriplet(self, nums: List[int]) -> bool:
        s = Solution()
        return s.increasingTriplet(nums)
