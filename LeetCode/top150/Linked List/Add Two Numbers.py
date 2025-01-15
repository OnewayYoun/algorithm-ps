from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]

    Input: l1 = [0], l2 = [0]
    Output: [0]

    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
    """

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            while head:
                head.next, head, prev = prev, head.next, head
            return prev

        new_l1 = reverse_linked_list(l1)
        new_l2 = reverse_linked_list(l2)

        val1 = ''
        val2 = ''
        while new_l1:
            val1 += str(new_l1.val)
            new_l1 = new_l1.next

        while new_l2:
            val2 += str(new_l2.val)
            new_l2 = new_l2.next

        sum_val = str(int(val1) + int(val2))
        dummy = tail = ListNode()
        for char in sum_val[::-1]:
            tail.next = ListNode()
            tail.next.val = int(char)
            tail = tail.next

        return dummy.next
