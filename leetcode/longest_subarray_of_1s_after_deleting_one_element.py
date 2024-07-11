# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        deleted = 0
        m = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                m = max(r + 1 - l - deleted, m)
                continue

            if deleted < 1:
                deleted += 1
                m = max(r + 1 - l - deleted, m)
                continue

            while nums[l] == 1:
                l += 1
            l += 1
            m = max(r + 1 - l - deleted, m)

        return m if m < len(nums) else len(nums) - 1
