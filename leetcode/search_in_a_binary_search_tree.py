# https://leetcode.com/problems/search-in-a-binary-search-tree
from typing import Optional

from leetcode.model.tree_node import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None:
            if root.val == val:
                return root

            if val < root.val:
                root = root.left
            else:
                root = root.right

        return None
