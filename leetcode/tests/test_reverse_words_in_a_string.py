from unittest import TestCase

from leetcode.reverse_words_in_a_string import Solution


class TestSolution(TestCase):

    def test_example1(self):
        result = self.reverseWords("the sky is blue")
        self.assertEqual(result, "blue is sky the")

    def test_example2(self):
        result = self.reverseWords("  hello world  ")
        self.assertEqual(result, "world hello")

    def test_example3(self):
        result = self.reverseWords("a good   example")
        self.assertEqual(result, "example good a")

    def test_empty(self):
        self.assertEqual(self.reverseWords(""), "")
        self.assertEqual(self.reverseWords(" "), "")
        self.assertEqual(self.reverseWords("  "), "")

    def test_one_word(self):
        self.assertEqual(self.reverseWords("word123"), "word123")
        self.assertEqual(self.reverseWords(" word123"), "word123")
        self.assertEqual(self.reverseWords("  word123"), "word123")
        self.assertEqual(self.reverseWords("word123 "), "word123")
        self.assertEqual(self.reverseWords("word123  "), "word123")
        self.assertEqual(self.reverseWords(" word123 "), "word123")
        self.assertEqual(self.reverseWords("  word123  "), "word123")

    def reverseWords(self, s: str) -> str:
        sol = Solution()
        return sol.reverseWords(s)
