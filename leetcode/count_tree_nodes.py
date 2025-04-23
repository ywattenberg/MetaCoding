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
    def find_mid(self, root: TreeNode, height: int) -> int:
        if height == 1:
            return 2 if not root.right else 3
        curr = root.right
        offset = 1
        while curr.left:
            curr = curr.left
            offset += 1
        if offset == height:
            res = self.find_mid(root.right, height - 1)
            # print(height, res + sum([2**i for i in range(height)]) + 1 )
            return res + sum([2**i for i in range(height)]) + 1
        else:
            res = self.find_mid(root.left, height - 1)
            # print(height, res + 2**(height - 2) + 1 )
            return res + sum([2**i for i in range(height - 1)]) + 1

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root or not root.left:
            return 0 if not root else 1
        levels = 0
        curr = root
        while curr:
            curr = curr.left
            levels += 1
        return self.find_mid(root, levels - 1)
