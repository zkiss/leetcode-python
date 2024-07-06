# https://leetcode.com/problems/n-th-tribonacci-number
class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0, 1, 1]
        if n - 2 > 0:
            tri += [0] * (n - 2)
        for i in range(3, n + 1):
            tri[i] = tri[i - 1] + tri[i - 2] + tri[i - 3]
        return tri[n]
