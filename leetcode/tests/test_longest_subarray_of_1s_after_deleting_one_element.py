from typing import List
from unittest import TestCase

from leetcode.longest_subarray_of_1s_after_deleting_one_element import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertEqual(self.longestSubarray([1, 1, 0, 1]), 3)

    def test_example2(self):
        self.assertEqual(self.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]), 5)

    def test_example3(self):
        self.assertEqual(self.longestSubarray([1, 1, 1]), 2)

    def test_min(self):
        self.assertEqual(self.longestSubarray([0]), 0)
        self.assertEqual(self.longestSubarray([1]), 0)
        self.assertEqual(self.longestSubarray([0, 0]), 0)
        self.assertEqual(self.longestSubarray([0, 1]), 1)
        self.assertEqual(self.longestSubarray([1, 0]), 1)
        self.assertEqual(self.longestSubarray([1, 1]), 1)

    def longestSubarray(self, nums: List[int]) -> int:
        s = Solution()
        return s.longestSubarray(nums)
