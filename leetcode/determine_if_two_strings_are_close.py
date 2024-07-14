# https://leetcode.com/problems/determine-if-two-strings-are-close
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = []
        c2 = []
        for c in set(word1):
            c1.append(word1.count(c))
            c2.append(word2.count(c))
        c1.sort()
        c2.sort()
        return c1 == c2
