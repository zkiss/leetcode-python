from typing import List
from unittest import TestCase

from leetcode.product_of_array_except_self import Solution


class TestSolution(TestCase):

    def test_example1(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(self.productExceptSelf(nums), [24, 12, 8, 6])

    def test_example2(self):
        nums = [-1, 1, 0, -3, 3]
        self.assertEqual(self.productExceptSelf(nums), [0, 0, 9, 0, 0])

    def test_minimal(self):
        self.assertEqual(self.productExceptSelf([5, 7]), [7, 5])

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = Solution()
        return sol.productExceptSelf(nums)
