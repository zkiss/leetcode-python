# https://leetcode.com/problems/daily-temperatures
from _bisect import bisect_right
from bisect import bisect
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack
        stack = [0]
        ans = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                ans[j] = i - j

            stack.append(i)

        return ans
