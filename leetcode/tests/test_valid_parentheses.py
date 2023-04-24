from unittest import TestCase

from leetcode.valid_parentheses import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertTrue(self.isValid("()"))

    def test_example2(self):
        self.assertTrue(self.isValid("()[]{}"))

    def test_example3(self):
        self.assertFalse(self.isValid("(]"))

    def test_one(self):
        self.assertFalse(self.isValid("("))

    def test_three(self):
        self.assertFalse(self.isValid("()["))

    def test_reversed(self):
        self.assertFalse(self.isValid(")("))

    def test_nested(self):
        self.assertTrue(self.isValid("({[]}[]{})"))

    def isValid(self, s: str) -> bool:
        sol = Solution()
        return sol.isValid(s)
