import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))

        dummy = cur = ListNode()

        while heap:
            val, idx, node = heapq.heappop(heap)
            cur.next, cur, node = node, node, node.next

            if node:
                heapq.heappush(heap, (node.val, idx, node))

        return dummy.next
