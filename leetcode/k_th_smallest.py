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
    def recurse(
        self,
        root: Optional[TreeNode],
        pos: int,
    ) -> Tuple[int, Optional[int]]:
        if not root:
            return pos, None
        pos, res = self.recurse(root.left, pos)
        if res is not None:
            return pos + 1, res
        elif pos == self.k:
            return pos + 1, root.val
        else:
            return self.recurse(root.right, pos + 1)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        return self.recurse(root, 1)[1]
