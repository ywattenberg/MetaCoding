from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val: int = val
        self.next: None | ListNode = next


class Solution:
    def delNextNode(self, prev: ListNode):
        if prev.next:
            prev.next = prev.next.next

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        seen = head.val - 1
        curr = head
        while curr.next:
            if seen == curr.val or curr.next.val == curr.val:
                if prev:
                    self.delNextNode(prev)
                else:
                    head = curr.next
            else:
                prev = curr
            seen = curr.val
            curr = curr.next

        if not prev:
            return None
        return head
