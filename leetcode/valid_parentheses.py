# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []

        for p in s:
            if p in pairs:  # open
                stack.append(pairs[p])
            else:  # close
                if len(stack) == 0:
                    return False

                if p != stack.pop():
                    return False

        return len(stack) == 0
