from typing import List
from unittest import TestCase

from leetcode.can_place_flowers import Solution


class TestSolution(TestCase):

    def test_example1(self):
        self.assertTrue(self.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))

    def test_example2(self):
        self.assertFalse(self.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))

    def test_minimal(self):
        self.assertTrue(self.canPlaceFlowers([0], 1))
        self.assertTrue(self.canPlaceFlowers([1], 0))
        self.assertFalse(self.canPlaceFlowers([1], 1))

    def test_no_space(self):
        self.assertFalse(self.canPlaceFlowers([1, 0], 1))
        self.assertFalse(self.canPlaceFlowers([0, 1], 1))

    def test_empty(self):
        self.assertTrue(self.canPlaceFlowers([0, 0, 0, 0, 0], 3))
        self.assertTrue(self.canPlaceFlowers([0, 0, 0, 0, 0, 0], 3))
        self.assertFalse(self.canPlaceFlowers([0, 0, 0, 0, 0, 0], 4))

    def test_left(self):
        self.assertTrue(self.canPlaceFlowers([1, 0, 0, 0, 0], 2))
        self.assertTrue(self.canPlaceFlowers([1, 0, 0, 0, 0, 0], 2))
        self.assertFalse(self.canPlaceFlowers([1, 0, 0, 0, 0, 0], 3))

    def test_right(self):
        self.assertTrue(self.canPlaceFlowers([0, 0, 0, 0, 1], 2))
        self.assertTrue(self.canPlaceFlowers([0, 0, 0, 0, 0, 1], 2))
        self.assertFalse(self.canPlaceFlowers([0, 0, 0, 0, 0, 1], 3))

    def test_fail1(self):
        self.assertFalse(self.canPlaceFlowers([0, 1, 0], 1))

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        sol = Solution()
        return sol.canPlaceFlowers(flowerbed, n)
