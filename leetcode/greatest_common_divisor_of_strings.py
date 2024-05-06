# https://leetcode.com/problems/greatest-common-divisor-of-strings
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 + str2 == str2 + str1:
            return ""

        return str1[0:self.gcd(len(str1), len(str2))]

    def gcd(self, a: int, b: int):
        while b != 0:
            _b = b
            b = a % _b
            a = _b

        return a
