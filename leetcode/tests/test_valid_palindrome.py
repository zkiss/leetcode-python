from unittest import TestCase

from leetcode.valid_palindrome import Solution


class TestSolution(TestCase):

    def test_example1(self):
        self.assertTrue(self.isPalindrome("A man, a plan, a canal: Panama"))

    def test_example2(self):
        self.assertFalse(self.isPalindrome("race a car"))

    def test_example3(self):
        self.assertTrue(self.isPalindrome(" "))

    def test_empty(self):
        self.assertTrue(self.isPalindrome(""))

    def test_nopal(self):
        self.assertFalse(self.isPalindrome("notapalindrome"))

    def test_odd(self):
        self.assertTrue(self.isPalindrome("abcba"))

    def test_even(self):
        self.assertTrue(self.isPalindrome("abba"))

    def test_one(self):
        self.assertTrue(self.isPalindrome("a"))

    def test_two(self):
        self.assertTrue(self.isPalindrome("bb"))

    def test_two_not(self):
        self.assertFalse(self.isPalindrome("bc"))

    def test_alnum(self):
        self.assertTrue(self.isPalindrome("a1b22b1a"))

    def test_alnum_not(self):
        self.assertFalse(self.isPalindrome("1a"))

    def isPalindrome(self, s: str) -> bool:
        sol = Solution()
        return sol.isPalindrome(s)
