# https://leetcode.com/problems/guess-number-higher-or-lower
from math import floor

PICKED = -1


def pick(num: int):
    global PICKED
    PICKED = num
    print(f"Picked {PICKED}")


def guess(num: int) -> int:
    global PICKED
    print(f"Guessing {num}, picked {PICKED}")
    if num < PICKED:
        return 1
    if num > PICKED:
        return -1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n

        while lo < hi:
            mid = lo + floor((hi - lo) / 2)
            r = guess(mid)
            if r == 0:
                return mid

            if r < 0:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
