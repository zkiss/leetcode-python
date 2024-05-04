from unittest import TestCase

from leetcode.climbing_stairs import Solution


class TestSolution(TestCase):

    def test_example1(self):
        self.assertEqual(self.climbStairs(2), 2)

    def test_example2(self):
        self.assertEqual(self.climbStairs(3), 3)

    def climbStairs(self, n: int) -> int:
        sol = Solution()
        return sol.climbStairs(n)
