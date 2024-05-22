# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        l = 0
        r = 0
        cnt = 0

        while r < k:
            if s[r] in vowels:
                cnt += 1
            r += 1

        m = cnt
        while r < len(s):
            diff = 0
            if s[l] in vowels:
                diff -= 1
            if s[r] in vowels:
                diff += 1
            cnt += diff
            m = max(m, cnt)
            l += 1
            r += 1

        return m
