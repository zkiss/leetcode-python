from unittest import TestCase

from leetcode.model.tree_node import TreeNode


class TestTreeNode(TestCase):
    def test_node(self):
        nums = [4, 2, 7, 1, 3]
        node = TreeNode.of(nums)
        self.assertEqual(
            "[4, 2, 7, 1, 3]",
            str(node)
        )
