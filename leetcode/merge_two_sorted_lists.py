from typing import Optional

from leetcode.listnode import ListNode


# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ret = None
        curr = None

        while list1 is not None or \
                list2 is not None:
            if list2 is None:
                c = list1
                list1 = list1.next
            elif list1 is None:
                c = list2
                list2 = list2.next
            elif list1.val < list2.val:
                c = list1
                list1 = list1.next
            else:
                c = list2
                list2 = list2.next

            if curr is None:
                curr = c
            else:
                curr.next = c
                curr = curr.next

            if ret is None:
                ret = curr

        return ret
