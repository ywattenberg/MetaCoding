# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val: int = val
        self.next: None | ListNode = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        pred: ListNode = head
        curr: ListNode = head.next

        while curr.val != left and curr.next:
            pred = curr
            curr = curr.next

        if curr.val != left:
            return head

        prev = pred
        while curr.next and curr.val != right:
            curr_n = curr.next
            curr.next = prev
            prev = curr
            curr = curr_n

        pred.next = curr.next
        curr.next = prev
        return head
