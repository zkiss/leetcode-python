# https://leetcode.com/problems/max-consecutive-ones-iii
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        flipped = 0
        m = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                m = max(m, r + 1 - l)
                continue

            if flipped < k:
                flipped += 1
                m = max(m, r + 1 - l)
                continue

            while nums[l] == 1:
                l += 1
            l += 1
            m = max(m, r + 1 - l)

        return m
