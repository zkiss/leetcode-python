from typing import List
from unittest import TestCase

from leetcode.kids_with_the_greatest_number_of_candies import Solution


class TestSolution(TestCase):

    def test_example1(self):
        result = self.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3)
        self.assertEqual(result, [True, True, True, False, True])

    def test_example2(self):
        result = self.kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1)
        self.assertEqual(result, [True, False, False, False, False])

    def test_example3(self):
        result = self.kidsWithCandies(candies=[12, 1, 12], extraCandies=10)
        self.assertEqual(result, [True, False, True])

    def test_multiwin(self):
        result = self.kidsWithCandies([2, 0], 2)
        self.assertEqual(result, [True, True])

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        sol = Solution()
        return sol.kidsWithCandies(candies, extraCandies)
