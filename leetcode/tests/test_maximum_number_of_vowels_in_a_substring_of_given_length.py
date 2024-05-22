from unittest import TestCase

from leetcode.maximum_number_of_vowels_in_a_substring_of_given_length import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertEqual(self.maxVowels("abciiidef", 3), 3)

    def test_example2(self):
        self.assertEqual(self.maxVowels("aeiou", 2), 2)

    def test_example3(self):
        self.assertEqual(self.maxVowels("leetcode", 3), 2)

    def test_no_vowels(self):
        self.assertEqual(self.maxVowels("bcdfghjkl", 3), 0)

    def test_all(self):
        self.assertEqual(self.maxVowels("aaaaaaaaa", 9), 9)
        self.assertEqual(self.maxVowels("bbbbbbbbb", 9), 0)
        self.assertEqual(self.maxVowels("ababababa", 9), 5)

    def test_minimal(self):
        self.assertEqual(self.maxVowels("a", 1), 1)
        self.assertEqual(self.maxVowels("b", 1), 0)

    def maxVowels(self, s: str, k: int) -> int:
        sol = Solution()
        return sol.maxVowels(s, k)
