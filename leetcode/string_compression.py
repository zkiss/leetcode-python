# https://leetcode.com/problems/string-compression
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 1
        curr = chars[0]
        length = 1
        count = 1
        for j in range(1, len(chars)):
            if curr == chars[j]:
                count += 1
            else:
                if count > 1:
                    for c in str(count):
                        chars[i] = c
                        length += 1
                        i += 1
                curr = chars[j]
                chars[i] = curr
                length += 1
                i += 1
                count = 1

        if count > 1:
            for c in str(count):
                chars[i] = c
                i += 1
                length += 1

        return length
