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
    def recursive(self, root: Optional[TreeNode]) -> Tuple[bool, float, float]:
        # Return is_valid, min, max
        if not root:
            return True, float('inf'), float('-inf')
        lval, lmin, lmax = self.recursive(root.left)
        if not lval:
            return False, 0, 0
        rval, rmin, rmax = self.recursive(root.right)
        if not rval:
            return False, 0, 0
        val = lval and rval
        val = val and lmax < root.val and rmin > root.val
        return val, min(lmin, root.val), max(rmax, root.val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recursive(root)[0]
