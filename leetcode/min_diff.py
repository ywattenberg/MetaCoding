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
        self, root: Optional[TreeNode]
    ) -> Tuple[int, int, int]:  # abs min, min, max
        if not root:
            return 10**6, 10**6, -(10**6)
        labs, lmin, lmax = self.recurse(root.left)
        rabs, rmin, rmax = self.recurse(root.right)
        return (
            min(labs, rabs, abs(root.val - lmax), abs(root.val - rmin)),
            min(lmin, root.val),
            max(rmax, root.val),
        )

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        return self.recurse(root)[0]
