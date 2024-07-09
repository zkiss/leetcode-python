# https://leetcode.com/problems/max-number-of-k-sum-pairs
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = {}
        ans = 0
        for n in nums:
            needed = k - n
            if needed in counts and counts[needed] > 0:
                c = counts[needed]
                counts[needed] = c - 1
                ans += 1
            else:
                c = 0
                if n in counts:
                    c = counts[n]
                counts[n] = c + 1

        return ans
