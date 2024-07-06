from unittest import TestCase

from leetcode.guess_number_higher_or_lower import Solution, pick


class TestSolution(TestCase):
    def test_example1(self):
        pick(6)
        self.assertEqual(self.guessNumber(10), 6)

    def test_example2(self):
        pick(1)
        self.assertEqual(self.guessNumber(1), 1)

    def test_example3(self):
        pick(1)
        self.assertEqual(self.guessNumber(2), 1)

    def test_hi(self):
        pick(10)
        self.assertEqual(self.guessNumber(10), 10)
        pick(9)
        self.assertEqual(self.guessNumber(9), 9)

    def test_lo(self):
        pick(1)
        self.assertEqual(self.guessNumber(10), 1)
        self.assertEqual(self.guessNumber(9), 1)

    def test_mid(self):
        pick(5)
        self.assertEqual(self.guessNumber(8), 5)
        self.assertEqual(self.guessNumber(9), 5)
        self.assertEqual(self.guessNumber(10), 5)

    def guessNumber(self, n: int) -> int:
        s = Solution()
        return s.guessNumber(n)
