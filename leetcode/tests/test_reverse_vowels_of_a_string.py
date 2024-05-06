from unittest import TestCase

from leetcode.reverse_vowels_of_a_string import Solution


class TestSolution(TestCase):

    def test_example1(self):
        self.assertEqual(self.reverseVowels("hello"), "holle")

    def test_example2(self):
        self.assertEqual(self.reverseVowels("leetcode"), "leotcede")

    def test_missing(self):
        self.assertEqual(self.reverseVowels("bcdfg"), "bcdfg")

    def test_empty(self):
        self.assertEqual(self.reverseVowels(""), "")

    def test_single(self):
        self.assertEqual(self.reverseVowels("abc"), "abc")

    def test_only_same(self):
        self.assertEqual(self.reverseVowels("aaa"), "aaa")

    def test_only_vowels(self):
        self.assertEqual(self.reverseVowels("aeoo"), "ooea")
        self.assertEqual(self.reverseVowels("AEOO"), "OOEA")

    def reverseVowels(self, s: str) -> str:
        sol = Solution()
        return sol.reverseVowels(s)
