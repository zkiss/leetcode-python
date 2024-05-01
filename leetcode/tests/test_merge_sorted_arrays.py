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

    def test_empties(self):
        num1 = []

        self.merge(num1, 0, [], 0)

        self.assertEqual(num1, [])

    def test_sames(self):
        num1 = [-1, -1, 0, 0, 0]

        self.merge(num1, 2, [-1, -1, -1], 3)

        self.assertEqual(num1, [-1, -1, -1, -1, -1])

    def test_reversed(self):
        num1 = [100, 100, 101, 102, 0, 0, 0]

        self.merge(num1, 4, [1, 2, 3], 3)

        self.assertEqual(num1, [1, 2, 3, 100, 100, 101, 102])

    def test_inorder(self):
        num1 = [1, 2, 3, 0, 0, 0]

        self.merge(num1, 3, [4, 5, 6], 3)

        self.assertEqual(num1, [1, 2, 3, 4, 5, 6])

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        s = Solution()
        s.merge(nums1, m, nums2, n)
