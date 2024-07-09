from typing import List
from unittest import TestCase

from leetcode.string_compression import Solution


class TestSolution(TestCase):
    def test_example1(self):
        arr = ["a", "a", "b", "b", "c", "c", "c"]
        self.assertEqual(self.compress(arr), 6)
        self.assertEqual(arr[:6], ["a", "2", "b", "2", "c", "3"])

    def test_example2(self):
        arr = ["a"]
        self.assertEqual(self.compress(arr), 1)
        self.assertEqual(arr, ["a"])

    def test_example3(self):
        arr = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        self.assertEqual(self.compress(arr), 4)
        self.assertEqual(arr[:4], ["a", "b", "1", "2"])

    def test_same(self):
        arr = ["a", "b", "c"]
        self.assertEqual(self.compress(arr), 3)
        self.assertEqual(arr[:3], ["a", "b", "c"])

    def test_alternate(self):
        arr = ["a", "b", "b", "a", "b", "a", "a", "a", "b", "b"]
        self.assertEqual(self.compress(arr), 9)
        self.assertEqual(arr[:9], ["a", "b", "2", "a", "b", "a", "3", "b", "2"])

    def compress(self, chars: List[str]) -> int:
        s = Solution()
        return s.compress(chars)
