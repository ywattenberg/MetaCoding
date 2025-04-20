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
    def recurse(self, root: Optional[TreeNode], digits: str = ''):
        if not root:
            return 0
        if not root.left and not root.right:
            return int(digits + str(root.val))
        return self.recurse(root.left, digits + str(root.val)) + self.recurse(
            root.right, digits + str(root.val)
        )

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.recurse(root)
