# https://leetcode.com/problems/move-zeroes
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        z = None
        for i in range(len(nums)):
            if nums[i] == 0:
                if z is None:
                    z = i
            else:
                if not z is None:
                    nums[z] = nums[i]
                    nums[i] = 0
                    z += 1
