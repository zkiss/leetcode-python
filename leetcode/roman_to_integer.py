# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) <= 1:
            match s:
                case 'I':
                    return 1
                case 'V':
                    return 5
                case 'X':
                    return 10
                case 'L':
                    return 50
                case 'C':
                    return 100
                case 'D':
                    return 500
                case 'M':
                    return 1000
                case _:
                    raise Exception("Unknown: " + s)

        idx = 0
        val = 0
        while idx < len(s):
            inc = self.romanToInt(s[idx])
            next = self.romanToInt(s[idx + 1]) \
                if idx + 1 < len(s) \
                else 0

            if next > inc:
                inc = next - inc
                idx += 2
            else:
                idx += 1

            val += inc

        return val
