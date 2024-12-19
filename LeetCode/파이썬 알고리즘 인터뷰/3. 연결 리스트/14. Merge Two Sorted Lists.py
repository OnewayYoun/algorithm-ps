from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

    Input: list1 = [], list2 = []
    Output: []

    Input: list1 = [], list2 = [0]
    Output: [0]
    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        tail = dummy_node

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # h = dummy_node.next
        # while h:
        #     print(h.val)
        #     h = h.next

        return dummy_node.next


n1, n2 = ListNode(1), ListNode(1)

n1.next = ListNode(2)
n1.next.next = ListNode(4)

n2.next = ListNode(3)
n2.next.next = ListNode(4)

print(Solution().mergeTwoLists(n1, n2))
