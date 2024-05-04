from unittest import TestCase

from leetcode.is_subsequence import Solution


class TestSolution(TestCase):

    def test_example1(self):
        self.assertTrue(self.isSubsequence("abc", "ahbgdc"))

    def test_example2(self):
        self.assertFalse(self.isSubsequence("axc", "ahbgdc"))

    def test_definition(self):
        self.assertTrue(self.isSubsequence("ace", "abcde"))
        self.assertFalse(self.isSubsequence("aec", "abcde"))

    def test_empty(self):
        self.assertTrue(self.isSubsequence("", "abc"))
        self.assertTrue(self.isSubsequence("", ""))
        self.assertFalse(self.isSubsequence("abc", ""))

    def test_sames(self):
        self.assertTrue(self.isSubsequence("aaa", "aaaa"))

    def test_exact(self):
        self.assertTrue(self.isSubsequence("aa", "aabbcc"))
        self.assertTrue(self.isSubsequence("bb", "aabbcc"))
        self.assertTrue(self.isSubsequence("cc", "aabbcc"))

    def test_larger(self):
        self.assertFalse(self.isSubsequence("abcde", "abc"))

    def test_same(self):
        self.assertTrue(self.isSubsequence("abc", "abc"))

    def test_fail1(self):
        self.assertFalse(self.isSubsequence("aaaaaa", "bbaaaa"))

    def isSubsequence(self, s: str, t: str) -> bool:
        sol = Solution()
        return sol.isSubsequence(s, t)
