from typing import Optional
from unittest import TestCase

from leetcode.model.tree_node import TreeNode
from leetcode.search_in_a_binary_search_tree import Solution


class TestSolution(TestCase):
    def test_example1(self):
        self.assertEqual(
            self.searchBST(TreeNode.of([4, 2, 7, 1, 3]), 2),
            TreeNode.of([2, 1, 3])
        )

    def test_example2(self):
        self.assertEqual(
            self.searchBST(TreeNode.of([4, 2, 7, 1, 3]), 5),
            None
        )

    def test_none(self):
        self.assertIsNone(self.searchBST(None, 0))

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        s = Solution()
        return s.searchBST(root, val)
