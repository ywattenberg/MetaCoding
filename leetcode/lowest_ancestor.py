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
        self, curr: Optional[TreeNode], p: TreeNode, q: TreeNode
    ) -> Tuple[TreeNode | None, bool, bool]:
        # This function will return in order LCA if one is found if p/q resp. is in this tree
        if not curr:
            return None, False, False
        left = self.recurse(curr.left, p, q)
        right = self.recurse(curr.right, p, q)

        if left[0] or right[0]:
            return left[0] if left[0] else right[0], True, True
        else:
            p_in = curr == p or left[1] or right[1]
            q_in = curr == q or left[2] or right[2]
            return curr if p_in and q_in else None, p_in, q_in

    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        return self.recurse(root, p, q)[0]
