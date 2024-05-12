# https://leetcode.com/problems/maximum-average-subarray-i
from builtins import max
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def avg(n: List[int]) -> float:
            a = n[0]
            for i in range(1, len(n)):
                a = a / (i + 1) * i + n[i] / (i + 1)
            return a

        a = avg(nums[0:k])
        m = a
        for i in range(k, len(nums)):
            a = (a * k - nums[i - k] + nums[i]) / k
            m = max(m, a)

        return m
