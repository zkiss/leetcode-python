from typing import List


# https://leetcode.com/problems/merge-sorted-array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        t = len(nums1) - 1

        while j >= 0:
            if i < 0:
                nums1[t] = nums2[j]
                j -= 1
            else:
                a = nums1[i]
                b = nums2[j]
                if a > b:
                    nums1[t] = a
                    i -= 1
                else:
                    nums1[t] = b
                    j -= 1
            t -= 1
