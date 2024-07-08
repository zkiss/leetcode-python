# https://leetcode.com/problems/online-stock-span
class StockSpanner:

    def __init__(self):
        self._stack = []
        self._idx = 0
        self._prices = []

    def next(self, price: int) -> int:
        while self._stack and self._prices[self._stack[-1]] <= price:
            self._stack.pop()

        ans = self._idx + 1
        if len(self._stack):
            ans = self._idx - self._stack[-1]

        self._stack.append(self._idx)

        self._prices.append(price)
        self._idx += 1
        return ans
