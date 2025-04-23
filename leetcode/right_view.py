# Definition for a binary tree node.
from typing import Optional, List


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
    def recurse(self, curr: Optional[TreeNode], level: int, depth: List[int]):
        if not curr:
            return depth
        if level >= len(depth):
            depth.append(curr.val)
        self.recurse(curr.right, level + 1, depth)
        self.recurse(curr.left, level + 1, depth)
        return depth

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.recurse(root, 0, [])
