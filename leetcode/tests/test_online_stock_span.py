from unittest import TestCase

from leetcode.online_stock_span import StockSpanner


class TestStockSpanner(TestCase):
    def test_example1(self):
        sp = StockSpanner()

        self.assertEqual(sp.next(100), 1)
        self.assertEqual(sp.next(80), 1)
        self.assertEqual(sp.next(60), 1)
        self.assertEqual(sp.next(70), 2)
        self.assertEqual(sp.next(60), 1)
        self.assertEqual(sp.next(75), 4)
        self.assertEqual(sp.next(85), 6)

    def test_example_text1(self):
        sp = StockSpanner()
        sp.next(7)
        sp.next(2)
        sp.next(1)
        sp.next(2)

        self.assertEqual(sp.next(2), 4)

    def test_example_text2(self):
        sp = StockSpanner()
        sp.next(7)
        sp.next(34)
        sp.next(1)
        sp.next(2)

        self.assertEqual(sp.next(8), 3)
