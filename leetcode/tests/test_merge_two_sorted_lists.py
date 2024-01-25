from typing import Optional
from unittest import TestCase

from leetcode.listnode import ListNode, list
from leetcode.merge_two_sorted_lists import Solution


class TestSolution(TestCase):

    def test_example1(self):
        list1 = list(1, 2, 4)
        list2 = list(1, 3, 4)

        result = self.mergeTwoLists(list1, list2)

        self.assertEqual(list(1, 1, 2, 3, 4, 4), result)

    def test_example2(self):
        result = self.mergeTwoLists(list(), list())

        self.assertEqual(list(), result)

    def test_example3(self):
        result = self.mergeTwoLists(list(), list(0))
        self.assertEqual(list(0), result)

    def test_second_empty(self):
        result = self.mergeTwoLists(list(1, 2, 3), list())
        self.assertEqual(list(1, 2, 3), result)

    def test_all_same(self):
        result = self.mergeTwoLists(list(1, 1), list(1, 1, 1))
        self.assertEqual(list(1, 1, 1, 1, 1), result)

    def test_sames2(self):
        result = self.mergeTwoLists(list(1, 1, 1), list(2, 2))
        self.assertEqual(list(1, 1, 1, 2, 2), result)

    def test_sames3(self):
        result = self.mergeTwoLists(list(2, 2, 2), list(1, 1))
        self.assertEqual(list(1, 1, 2, 2, 2), result)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        s = Solution()
        return s.mergeTwoLists(list1, list2)
