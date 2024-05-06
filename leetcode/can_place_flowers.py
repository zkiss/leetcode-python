from typing import List


# https://leetcode.com/problems/can-place-flowers
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def space(l: int, r: int) -> int:
            return (r - l + 2) // 2

        l = 0
        i = 0
        s = 0
        while i < len(flowerbed):
            if flowerbed[i] != 0:
                r = i - 2
                s += space(l, r)
                l = i + 2

            i += 1

        return s + space(l, i - 1) >= n
