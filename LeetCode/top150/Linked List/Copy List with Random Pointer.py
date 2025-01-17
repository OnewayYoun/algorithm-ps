from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pointer_dict = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            pointer_dict[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            pointer_dict[cur].next = pointer_dict[cur.next]
            pointer_dict[cur].random = pointer_dict[cur.random]
            cur = cur.next

        return pointer_dict[head]
