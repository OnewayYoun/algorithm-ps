from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cache = {}
        i = 1
        cur = head
        while cur:
            cache[i] = cur
            i += 1
            cur = cur.next

        length = len(cache)
        if n == 1:
            if length == 1:
                return None
            else:
                cache[length - n].next = None
                return head

        if length - n == 0:
            return head.next
        cache[length - n].next = cache[length - n + 2]
        return head
