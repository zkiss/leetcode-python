# https://leetcode.com/problems/unique-number-of-occurrences
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = {}
        for i in arr:
            cur = cnt[i] if i in cnt else 0
            cur += 1
            cnt[i] = cur
        uq = set(cnt.values())
        return len(uq) == len(cnt)
