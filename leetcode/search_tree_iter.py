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


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.callstack: List[TreeNode] = []
        self._fill_stack(root)

    def _fill_stack(self, curr: Optional[TreeNode]):
        if not curr:
            return
        self._fill_stack(curr.left)
        self.callstack.append(curr)
        self._fill_stack(curr.right)
        return

    def next(self) -> int:
        return self.callstack.popleft().val

    def hasNext(self) -> bool:
        return len(self.callstack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
