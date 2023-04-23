from unittest import TestCase

from leetcode.roman_to_integer import Solution


class TestSolution(TestCase):
    def test_example1(self):
        result = self.romanToInt("III")
        self.assertEqual(result, 3)

    def test_example2(self):
        result = self.romanToInt("LVIII")
        self.assertEqual(result, 58)

    def test_example3(self):
        result = self.romanToInt("MCMXCIV")
        self.assertEqual(result, 1994)

    def romanToInt(self, roman: str) -> int:
        s = Solution()
        return s.romanToInt(roman)
