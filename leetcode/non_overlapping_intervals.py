# https://leetcode.com/problems/non-overlapping-intervals
import bisect
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0

        intervals.sort(key=lambda i: i[0])
        removed = 0
        first = intervals[0]

        def start(interval: List[int]) -> int:
            return interval[0]

        def end(interval: List[int]) -> int:
            return interval[1]

        for i in range(1, len(intervals)):
            second = intervals[i]

            if end(first) <= start(second):
                first = second
                continue

            if end(first) < end(second):
                removed += 1
                continue

            removed += 1
            first = second

        return removed
