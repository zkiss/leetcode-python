from typing import List
from unittest import TestCase

from leetcode.move_zeroes import Solution


class TestSolution(TestCase):

    def test_example1(self):
        nums = [0, 1, 0, 3, 12]
        self.moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_example2(self):
        nums = [0]
        self.moveZeroes(nums)
        self.assertEqual(nums, [0])

    def test_no_zeroes(self):
        nums = [1, 2, 3, 4]
        self.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4])

    def test_one_nonzero_end(self):
        nums = [0, 0, 0, 0, 1]
        self.moveZeroes(nums)
        self.assertEqual(nums, [1, 0, 0, 0, 0])

    def test_all_zeroes(self):
        nums = [0, 0, 0]
        self.moveZeroes(nums)
        self.assertEqual(nums, [0, 0, 0])

    def moveZeroes(self, nums: List[int]) -> None:
        sol = Solution()
        sol.moveZeroes(nums)
