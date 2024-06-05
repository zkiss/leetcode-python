from typing import List
from unittest import TestCase

from leetcode.find_the_difference_of_two_arrays import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertEqual(
            self.findDifference([1, 2, 3], [2, 4, 6]),
            [[1, 3], [4, 6]])

    def test_example2(self):
        self.assertEqual(
            self.findDifference(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]),
            [[3], []])

    def test_minimal(self):
        self.assertEqual(
            self.findDifference(nums1=[1], nums2=[2]),
            [[1], [2]])
        self.assertEqual(
            self.findDifference(nums1=[1], nums2=[1]),
            [[], []])

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        sol = Solution()
        return sol.findDifference(nums1, nums2)
