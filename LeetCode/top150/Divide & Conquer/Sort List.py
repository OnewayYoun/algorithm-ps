from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_mid(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(node1, node2):
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

        if not head or not head.next:
            return head

        mid = get_mid(head)
        tmp = mid.next
        mid.next = None

        left = head
        right = tmp
        left = self.sortList(left)
        right = self.sortList(right)

        return merge(left, right)
























class Solution1:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_mid(head_node: ListNode) -> ListNode:
            slow = fast = head_node
            fast = fast.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def merge(left: ListNode, right: ListNode) -> ListNode:
            dummy = tail = ListNode()

            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next

            if left:
                tail.next = left
            else:
                tail.next = right

            return dummy.next

        if not head or not head.next:
            return head

        left = head
        right = get_mid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)

        return merge(left, right)


