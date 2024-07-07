# https://leetcode.com/problems/increasing-triplet-subsequence

import math
from builtins import min
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        import builtins
        max = nums[len(nums) - 1]
        maxs = [None] * len(nums)
        maxs[len(nums) - 1] = max
        for i in range(len(nums) - 2, -1, -1):
            max = builtins.max(max, nums[i])
            maxs[i] = max

        min = nums[0]
        for i in range(1, len(nums) - 1):
            min = builtins.min(min, nums[i])
            if min < nums[i] < maxs[i + 1]:
                return True

        return False
