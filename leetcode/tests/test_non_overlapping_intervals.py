from typing import List
from unittest import TestCase

from leetcode.non_overlapping_intervals import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertEqual(self.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)

    def test_example2(self):
        self.assertEqual(self.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]), 2)

    def test_example3(self):
        self.assertEqual(self.eraseOverlapIntervals([[1, 2], [2, 3]]), 0)

    def test_min(self):
        self.assertEqual(self.eraseOverlapIntervals([[1, 2]]), 0)

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        s = Solution()
        return s.eraseOverlapIntervals(intervals)
