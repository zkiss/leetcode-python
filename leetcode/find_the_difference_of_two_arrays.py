# https://leetcode.com/problems/find-the-difference-of-two-arrays
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a1 = set(nums1)
        a2 = set(nums2)
        a1.difference_update(set(nums2))
        a2.difference_update(set(nums1))
        return [list(a1), list(a2)]
