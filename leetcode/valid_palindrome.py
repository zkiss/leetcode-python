# https://leetcode.com/problems/valid-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            l = s[i]
            if not l.isalnum():
                i += 1
                continue
            r = s[j]
            if not r.isalnum():
                j -= 1
                continue

            l = l.lower()
            r = r.lower()

            if l != r:
                return False
            i += 1
            j -= 1

        return True
