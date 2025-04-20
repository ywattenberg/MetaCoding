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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            curr = preorder.pop(0)
            idx = inorder.index(curr)
            return TreeNode(
                curr,
                self.buildTree(preorder, inorder[:idx]),
                self.buildTree(preorder, inorder[idx + 1 :]),
            )
