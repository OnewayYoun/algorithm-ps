from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS O(N)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    # BFS O(N)
    def countNodes1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        dq = deque()
        dq.append(root)
        cnt = 1

        while dq:
            node = dq.popleft()
            if node.left:
                dq.append(node.left)
                cnt += 1
            if node.right:
                dq.append(node.right)
                cnt += 1
        return cnt

    # DFS O(log(n) * log(n))
    def countNodes2(self, root: Optional[TreeNode]) -> int:
        def get_left_height(node):
            if not node:
                return 0
            return get_left_height(node.left) + 1

        def get_right_height(node):
            if not node:
                return 0
            return get_right_height(node.right) + 1

        l, r = get_left_height(root), get_right_height(root)

        if l == r:
            return (2 ** l) - 1
        else:
            return self.countNodes2(root.left) + self.countNodes2(root.right) + 1
