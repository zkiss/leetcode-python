from typing import List
from unittest import TestCase

from leetcode.daily_temperatures import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertEqual(
            self.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0]
        )

    def test_example2(self):
        self.assertEqual(
            self.dailyTemperatures([30, 40, 50, 60]),
            [1, 1, 1, 0]
        )

    def test_example3(self):
        self.assertEqual(
            self.dailyTemperatures([30, 60, 90]),
            [1, 1, 0]
        )

    def test_min(self):
        self.assertEqual(self.dailyTemperatures([10]), [0])

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = Solution()
        return s.dailyTemperatures(temperatures)
