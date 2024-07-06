# https://leetcode.com/problems/n-th-tribonacci-number
class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1
        if n == 0:
            return 0
        for i in range(3, n + 1):
            t0, t1, t2 = t1, t2, (t0 + t1 + t2)
        return t2
