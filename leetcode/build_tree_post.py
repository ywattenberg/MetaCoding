# Definition for a binary tree node.
from typing import Optional, List, Tuple


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
    def helper(self, inord, postord):
        if inord:
            curr = postord.pop()
            idx = self.pos[curr]
            right = (self.helper(inord[idx + 1 :], postord),)
            left = (self.helper(inord[:idx], postord),)
            return TreeNode(curr, left, right)

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.pos = {val: i for i, val in enumerate(inorder)}
        return self.helper(inorder, postorder)
