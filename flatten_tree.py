# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional['TreeNode'] = None,
        right: Optional['TreeNode'] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recurse(self, node: TreeNode) -> TreeNode:
        if node.left:
            last = self.recurse(node)
            last.right = node.right
            node.right = node.left
            return self.recurse(last.right) if last.right else last
        else:
            return self.recurse(node.right) if node.right else node

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
