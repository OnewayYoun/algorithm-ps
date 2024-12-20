# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Input: head = [3,2,0,-4], pos = 1
    Output: true

    Input: head = [1,2], pos = 0
    Output: true

    Input: head = [1], pos = -1
    Output: false
    """

    # space complexity O(N)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False

    # space complexity O(1)
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
