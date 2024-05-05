from unittest import TestCase

from leetcode.merge_strings_alternately import Solution


class TestSolution(TestCase):

    def test_example1(self):
        result = self.mergeAlternately(word1="abc", word2="pqr")
        self.assertEqual(result, "apbqcr")

    def test_example2(self):
        result = self.mergeAlternately(word1="ab", word2="pqrs")
        self.assertEqual(result, "apbqrs")

    def test_example3(self):
        result = self.mergeAlternately(word1="abcd", word2="pq")
        self.assertEqual(result, "apbqcd")

    def test_empty(self):
        self.assertEqual(self.mergeAlternately("", "ab"), "ab")
        self.assertEqual(self.mergeAlternately("ab", ""), "ab")
        self.assertEqual(self.mergeAlternately("", ""), "")

    def mergeAlternately(self, word1: str, word2: str) -> str:
        sol = Solution()
        return sol.mergeAlternately(word1, word2)
