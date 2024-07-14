from unittest import TestCase

from leetcode.determine_if_two_strings_are_close import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertTrue(self.closeStrings(word1="abc", word2="bca"))

    def test_example2(self):
        self.assertFalse(self.closeStrings(word1="a", word2="aa"))

    def test_example3(self):
        self.assertTrue(self.closeStrings(word1="cabbba", word2="abbccc"))

    def closeStrings(self, word1: str, word2: str) -> bool:
        s = Solution()
        return s.closeStrings(word1, word2)
