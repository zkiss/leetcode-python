from typing import List
from unittest import TestCase

from leetcode.keys_and_rooms import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertTrue(self.canVisitAllRooms([[1], [2], [3], []]))

    def test_example2(self):
        self.assertFalse(self.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))

    def test_min(self):
        self.assertTrue(self.canVisitAllRooms([[1], []]))
        self.assertFalse(self.canVisitAllRooms([[], []]))

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        s = Solution()
        return s.canVisitAllRooms(rooms)
