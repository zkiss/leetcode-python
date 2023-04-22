from unittest import TestCase

from leetcode.two_sum import Solution


class TestSolution(TestCase):
    def test_example_1(self):
        s = Solution()
        result = s.twoSum([2, 7, 11, 15], 9)
        self.assertCountEqual(result, [0, 1])

    def test_example_2(self):
        s = Solution()
        result = s.twoSum([3, 2, 4], 6)
        self.assertCountEqual(result, [1, 2])

    def test_example_3(self):
        s = Solution()
        result = s.twoSum([3, 3], 6)
        self.assertCountEqual(result, [0, 1])
