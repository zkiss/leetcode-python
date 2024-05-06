from unittest import TestCase

from leetcode.greatest_common_divisor_of_strings import Solution


class TestSolution(TestCase):

    def test_example1(self):
        result = self.gcdOfStrings(str1="ABCABC", str2="ABC")
        self.assertEqual(result, "ABC")

    def test_example2(self):
        result = self.gcdOfStrings(str1="ABABAB", str2="ABAB")
        self.assertEqual(result, "AB")

    def test_example3(self):
        result = self.gcdOfStrings(str1="LEET", str2="CODE")
        self.assertEqual(result, "")

    def test_almost(self):
        self.assertEqual(self.gcdOfStrings("ABABAB", "ABABC"), "")
        self.assertEqual(self.gcdOfStrings("ABABABC", "ABAB"), "")

    def test_repeating(self):
        self.assertEqual(self.gcdOfStrings("ABABABAB", "ABAB"), "ABAB")

    def test_sames(self):
        self.assertEqual(self.gcdOfStrings("ABCABC", "ABCABC"), "ABCABC")

    def test_longs_shorter_gcd(self):
        self.assertEqual(self.gcdOfStrings(
            "ABABABABABABABABABABABABABABABABABABAB",
            "ABABABABABABABABABABABABABABABABAB"),
            "AB"
        )

    def test_longs_no_gcd(self):
        self.assertEqual(self.gcdOfStrings(
            "ABABABABABABACBABABABABABABABABABABABAB",
            "ABABABABABABACBABABABABABABABABABAB"),
            ""
        )

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        sol = Solution()
        return sol.gcdOfStrings(str1, str2)
