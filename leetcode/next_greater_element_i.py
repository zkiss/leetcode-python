# https://leetcode.com/problems/next-greater-element-i
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # monotonic stack
        stack = [0]
        answers = {}

        for i in range(1, len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                biggest_prev = stack.pop()
                answers[nums2[biggest_prev]] = nums2[i]

            stack.append(i)

        for i in range(len(nums1)):
            ans = -1
            if nums1[i] in answers:
                ans = answers[nums1[i]]
            nums1[i] = ans

        return nums1
