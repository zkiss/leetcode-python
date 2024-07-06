from unittest import TestCase

from leetcode.n_th_tribonacci_number import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertEqual(self.tribonacci(4), 4)

    def test_example2(self):
        self.assertEqual(self.tribonacci(25), 1389537)

    def test_start(self):
        self.assertEqual(self.tribonacci(0), 0)
        self.assertEqual(self.tribonacci(1), 1)
        self.assertEqual(self.tribonacci(2), 1)
        self.assertEqual(self.tribonacci(3), 2)
        self.assertEqual(self.tribonacci(4), 4)
        self.assertEqual(self.tribonacci(5), 7)

    def tribonacci(self, n: int) -> int:
        s = Solution()
        return s.tribonacci(n)
