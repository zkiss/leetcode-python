from typing import List
from unittest import TestCase

from leetcode.unique_number_of_occurrences import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertTrue(self.uniqueOccurrences([1, 2, 2, 1, 1, 3]))

    def test_example2(self):
        self.assertFalse(self.uniqueOccurrences([1, 2]))

    def test_example3(self):
        self.assertTrue(self.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = Solution()
        return s.uniqueOccurrences(arr)
