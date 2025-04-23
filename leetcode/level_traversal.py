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
    def recurse(self, curr: Optional[TreeNode], level: int, nodes: List[List[int]]):
        if not curr:
            return nodes
        if len(nodes) <= level:
            nodes.append([curr.val])
        else:
            nodes[level].append(curr.val)
        self.recurse(curr.left, level + 1, nodes)
        self.recurse(curr.right, level + 1, nodes)
        return nodes

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.recurse(root, 0, [])
