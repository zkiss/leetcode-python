from typing import List
from unittest import TestCase

from leetcode.max_number_of_k_sum_pairs import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertEqual(self.maxOperations(nums=[1, 2, 3, 4], k=5), 2)

    def test_example2(self):
        self.assertEqual(self.maxOperations(nums=[3, 1, 3, 4, 3], k=6), 1)

    def maxOperations(self, nums: List[int], k: int) -> int:
        s = Solution()
        return s.maxOperations(nums, k)
