from typing import List
from unittest import TestCase

from leetcode.find_the_highest_altitude import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertEqual(self.largestAltitude([-5, 1, 5, 0, -7]), 1)

    def test_example2(self):
        self.assertEqual(self.largestAltitude([-4, -3, -2, -1, 4, 3, 2]), 0)

    def test_no_move(self):
        self.assertEqual(self.largestAltitude([0, 0, 0]), 0)

    def test_descent_only(self):
        self.assertEqual(self.largestAltitude([-1, -1, -1]), 0)

    def test_ascent_only(self):
        self.assertEqual(self.largestAltitude([1, 1, 1]), 3)

    def largestAltitude(self, gain: List[int]) -> int:
        sol = Solution()
        return sol.largestAltitude(gain)
