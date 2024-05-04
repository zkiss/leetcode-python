# https://leetcode.com/problems/is-subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s):
            a = s[i]
            while j < len(t) and a != t[j]:
                j += 1

            if j >= len(t):
                return False

            j += 1
            i += 1

        return i == len(s)
