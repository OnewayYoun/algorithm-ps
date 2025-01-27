from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or (right - left) == 0:
            return head

        cnt = 1
        cur = head
        starting_head = None
        while cur:
            if cnt + 1 == left:
                starting_head = cur
            if cnt == right:
                break
            cur = cur.next
            cnt += 1

        prev = cur.next
        if starting_head:
            node = starting_head.next
        else:
            node = head

        for _ in range(right - left + 1):
            node.next, node, prev = prev, node.next, node

        if starting_head:
            starting_head.next = prev
        return head if left > 1 else prev
