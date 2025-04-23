# Definition for a binary tree node.
from typing import Optional, Tuple


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
    def recurse(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        if not root:
            return -1001, -1001
        l, r = self.recurse(root.left), self.recurse(root.right)
        max_with_root = root.val
        max_with_root += max(l[1], r[1], 0)
        return max(
            l[0], r[0], max(l[1], 0) + max(r[1], 0) + root.val, max_with_root
        ), max_with_root

    def maxPathSum(self, root: TreeNode):
        return self.recurse(root)[0]
