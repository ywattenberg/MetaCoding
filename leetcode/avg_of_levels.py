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
    def recurse(self, curr: Optional[TreeNode], level:int, nodes:List[Tuple[int, int]]):
        if not curr:
            return
        if len(nodes) <=: level:
            nodes.append((curr.val, 1))
        else:
            pair = nodes[level]
            nodes[level] = (pair[0] + curr.val, pair[1] + 1)
        self.recurse(curr.left, level+1, nodes)
        self.recurse(curr.right, level+1, nodes)
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        nodes = []
        self.recurse(root, 0, nodes)
        return [a/b for a,b in nodes]
