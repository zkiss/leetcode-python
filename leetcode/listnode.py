from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        s = f"{self.val}"
        c = self.next
        while c is not None:
            s = f"{s} -> {c.val}"
            c = c.next
        return s

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False

        if self.val != other.val:
            return False

        if self.next is None:
            return other.next is None
        else:
            return self.next.__eq__(other.next)


def list(*args) -> Optional[ListNode]:
    ret = None
    curr = ret

    for n in args:
        if not isinstance(n, int):
            raise TypeError("Only int allowed")

        if curr is None:
            curr = ListNode(val=n)
        else:
            curr.next = ListNode(val=n)
            curr = curr.next

        if ret is None:
            ret = curr

    return ret
