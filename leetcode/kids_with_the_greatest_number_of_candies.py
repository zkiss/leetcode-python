from typing import List


# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        def max(l: List[int]) -> int:
            r = None
            for i in l:
                if r is None or i > r:
                    r = i
            return r

        m = max(candies)
        res = [False] * len(candies)
        for i in range(0, len(candies)):
            res[i] = candies[i] + extraCandies >= m

        return res
