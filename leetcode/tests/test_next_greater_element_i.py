from typing import List
from unittest import TestCase

from leetcode.next_greater_element_i import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertEqual(
            self.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]),
            [-1, 3, -1]
        )

    def test_example2(self):
        self.assertEqual(
            self.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]),
            [3, -1]
        )

    def test_min(self):
        self.assertEqual(
            self.nextGreaterElement(nums1=[1], nums2=[1]),
            [-1]
        )

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = Solution()
        return s.nextGreaterElement(nums1, nums2)
