from typing import List
from unittest import TestCase

from leetcode.longest_common_prefix import Solution


class TestSolution(TestCase):
    def test_example1(self):
        result = self.longestCommonPrefix(["flower", "flow", "flight"])
        self.assertEqual(result, "fl")

    def test_example2(self):
        result = self.longestCommonPrefix(["dog", "racecar", "car"])
        self.assertEqual(result, "")

    def test_single(self):
        result = self.longestCommonPrefix(["asdasd"])
        self.assertEqual(result, "asdasd")

    def test_empty(self):
        result = self.longestCommonPrefix([""])
        self.assertEqual(result, "")

    def test_all_same(self):
        result = self.longestCommonPrefix(["asd", "asd", "asd"])
        self.assertEqual(result, "asd")

    def test_error1(self):
        result = self.longestCommonPrefix(["", "b"])
        self.assertEqual(result, "")

    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = Solution()
        return s.longestCommonPrefix(strs)
