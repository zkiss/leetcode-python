# https://leetcode.com/problems/determine-if-two-strings-are-close
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def counts(iterable) -> dict:
            cnt = {}
            for c in iterable:
                curr = cnt[c] if c in cnt else 0
                cnt[c] = curr + 1
            return cnt

        c1 = counts(word1)
        c2 = counts(word2)

        if c1.keys() != c2.keys():
            return False

        if counts(c1.values()) != counts(c2.values()):
            return False

        return True
