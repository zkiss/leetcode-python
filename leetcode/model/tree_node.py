from typing import List


class TreeNode:

    @staticmethod
    def of(vals: List[int]):
        nodes = [TreeNode() for _ in vals]
        for i in range(len(vals)):
            nodes[i].val = vals[i]
            i_left = i * 2 + 1
            i_right = i * 2 + 2
            if i_left < len(nodes):
                nodes[i].left = nodes[i_left]
            if i_right < len(nodes):
                nodes[i].right = nodes[i_right]
        return nodes[0]

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, __value) -> bool:
        if not isinstance(__value, TreeNode):
            return False
        return self.val == __value.val \
            and self.left == __value.left \
            and self.right == __value.right

    def __str__(self) -> str:
        q = [self]
        nums = []
        while len(q) > 0:
            cur = q.pop(0)
            nums.append(cur.val)
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)

        return str(nums)
