# https://leetcode.com/problems/find-the-highest-altitude
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        m = alt
        for delta in gain:
            alt += delta
            m = max(alt, m)
        return m
