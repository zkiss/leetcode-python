# https://leetcode.com/problems/product-of-array-except-self
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_l = [0] * len(nums)
        prod_l[0] = nums[0]
        for i in range(1, len(nums)):
            prod_l[i] = prod_l[i - 1] * nums[i]

        prod_r = [0] * len(nums)
        prod_r[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, 0, -1):
            prod_r[i] = prod_r[i + 1] * nums[i]

        ret = [0] * len(nums)
        for i in range(len(nums)):
            l = 1
            if i > 0:
                l = prod_l[i - 1]
            r = 1
            if i < len(nums) - 1:
                r = prod_r[i + 1]

            ret[i] = l * r

        return ret
