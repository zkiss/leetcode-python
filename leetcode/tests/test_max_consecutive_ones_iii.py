from typing import List
from unittest import TestCase

from leetcode.max_consecutive_ones_iii import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertEqual(self.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2), 6)

    def test_example2(self):
        self.assertEqual(self.longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3), 10)

    def test_min(self):
        self.assertEqual(self.longestOnes(nums=[0], k=0), 0)
        self.assertEqual(self.longestOnes(nums=[1], k=0), 1)

    def test_allsames(self):
        self.assertEqual(self.longestOnes(nums=[0, 0, 0, 0, 0, 0], k=3), 3)
        self.assertEqual(self.longestOnes(nums=[0, 0, 0, 0, 0, 0], k=0), 0)
        self.assertEqual(self.longestOnes(nums=[0, 0, 0, 0, 0, 0], k=10), 6)
        self.assertEqual(self.longestOnes(nums=[1, 1, 1, 1, 1, 1], k=0), 6)
        self.assertEqual(self.longestOnes(nums=[1, 1, 1, 1, 1, 1], k=10), 6)

    def test_fail1(self):
        self.assertEqual(
            self.longestOnes(
                nums=[1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0,
                      1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
                k=10
            ),
            30
        )

    def longestOnes(self, nums: List[int], k: int) -> int:
        s = Solution()
        return s.longestOnes(nums, k)
