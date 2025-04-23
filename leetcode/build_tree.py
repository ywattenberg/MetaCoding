# Definition for a binary tree node.
from typing import Optional, List, Tuple
from collections import deque


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: 'Node' = None,
        right: 'Node' = None,
        next: 'Node' = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def recurse(self, node: Optional[Node], next: deque[Node]):
        if not node:
            return node
        if len(next) > 0:
            node.next = next.popleft()
        self.recurse(node.right, next)
        self.recurse(node.left, next)
        next.appendleft(node)
        return node

    def connect(self, root: 'Node') -> 'Node':
        return self.recurse(root, deque())
