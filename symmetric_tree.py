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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue_l = [root.left]
        queue_r = [root.right]
        while len(queue_l) > 0 and len(queue_r) > 0 and queue_r[-1] and queue_r[-1]:
            l = queue_l.pop()
            r = queue_r.pop()
            if r.val != l.val:
                return False
            if r.left or l.right:
                queue_l.append(l.right)
                queue_r.append(r.left)
            if r.right or l.left:
                queue_l.append(l.left)
                queue_r.append(r.right)
        if len(queue_l) or len(queue_r):
            return False
        return True

    def recursive(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        elif not left or not right or left.val != right.val:
            return False

        return self.recursive(left.right, right.left) and self.recursive(
            left.left, right.right
        )
