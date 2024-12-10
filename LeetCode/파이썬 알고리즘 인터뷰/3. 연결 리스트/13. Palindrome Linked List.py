# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Input: head = [1,2,2,1]
    Output: true

    Input: head = [1,2]
    Output: false
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        return tmp == tmp[::-1]

    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        left, right = head, prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

# [1,2,2,1]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

print(Solution().isPalindrome(head))
print(Solution().isPalindrome1(head))