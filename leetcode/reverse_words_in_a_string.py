# https://leetcode.com/problems/reverse-words-in-a-string
class Solution:
    def reverseWords(self, s: str) -> str:
        l = 0
        i = 0
        rev = []
        while i < len(s):
            if s[i] == ' ':
                if l < i:
                    rev.insert(0, s[l:i])
                l = i + 1
            i += 1

        if l < i:
            rev.insert(0, s[l:i])

        return ' '.join(rev)
