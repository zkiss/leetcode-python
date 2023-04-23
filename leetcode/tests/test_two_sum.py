from unittest import TestCase

from leetcode.two_sum import Solution


class TestSolution(TestCase):
    solution = Solution()

    def test_example_1(self):
        result = self.solution.twoSum([2, 7, 11, 15], 9)
        self.assertCountEqual(result, [0, 1])

    def test_example_2(self):
        result = self.solution.twoSum([3, 2, 4], 6)
        self.assertCountEqual(result, [1, 2])

    def test_example_3(self):
        result = self.solution.twoSum([3, 3], 6)
        self.assertCountEqual(result, [0, 1])

    def test_minimal(self):
        result = self.solution.twoSum([2, 3], 5)
        self.assertCountEqual(result, [0, 1])

    def test_negatives(self):
        result = self.solution.twoSum([-3, -1, 0, -4], -3)
        self.assertCountEqual(result, [0, 2])
