# https://leetcode.com/problems/find-pivot-index
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = [0] * len(nums)
        sum = 0
        for i in range(len(nums) - 1, -1, -1):
            right[i] = sum
            sum += nums[i]

        left = [0] * len(nums)
        sum = 0
        for i in range(0, len(nums)):
            left[i] = sum
            sum += nums[i]

            if left[i] == right[i]:
                return i

        return -1
