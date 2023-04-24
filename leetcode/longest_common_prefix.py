from typing import List


# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs.pop()

        for s in strs:
            if len(prefix) > len(s):
                prefix = prefix[0:len(s)]
            for i in range(len(prefix)):
                if s[i] != prefix[i]:
                    prefix = s[0:i]
                    break
            if len(prefix) == 0:
                return prefix

        return prefix
