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

    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_list = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_list.append(self.merge(list1, list2))
            lists = merged_list
        return lists[0]

    def merge(self, node1, node2):
        dummy = tail = ListNode()

        while node1 and node2:
            if node1.val < node2.val:
                tail.next = node1
                node1 = node1.next
            else:
                tail.next = node2
                node2 = node2.next
            tail = tail.next

        tail.next = node1 or node2
        return dummy.next
