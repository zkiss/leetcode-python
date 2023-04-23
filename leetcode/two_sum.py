from typing import List


# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i in range(len(nums)):
            needs = target - nums[i]
            if needs in dict:
                return [i, dict[needs]]

            dict[nums[i]] = i

        raise Exception("No solution")
