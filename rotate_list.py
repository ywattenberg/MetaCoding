# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        prev = head
        curr: ListNode = head.next

        while curr.next:
            curr_n = curr.next
            curr.next = prev
            prev = curr
            curr = curr_n
        curr.next = prev
        return curr

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n = 0
        begin = head
        while begin:
            n += 1
            begin = begin.next
        k = k % n
        begin = head
        end = head
        for _ in range(k):
            if not end.next:
                break
            end = end.next

        while end.next and k > 0:
            k -= 1
            begin = begin.next
            end = end.next

        new_start = self.reverseList(begin.next)

        begin.next = head
        return new_start
