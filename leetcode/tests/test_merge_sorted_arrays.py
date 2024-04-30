from typing import List
from unittest import TestCase

from leetcode.merge_sorted_arrays import Solution


class TestSolution(TestCase):

    def test_example1(self):
        num1 = [1, 2, 3, 0, 0, 0]

        self.merge(num1, 3, [2, 5, 6], 3)

        self.assertEqual(num1, [1, 2, 2, 3, 5, 6])

    def test_example2(self):
        num1 = [1]

        self.merge(num1, 1, [], 0)

        self.assertEqual(num1, [1])

    def test_example3(self):
        num1 = [0]

        self.merge(num1, 0, [1], 1)

        self.assertEqual(num1, [1])

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        s = Solution()
        s.merge(nums1, m, nums2, n)
