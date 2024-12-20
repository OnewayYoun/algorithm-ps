from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # BFS
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        dq = deque()
        dq.append([root, 1])
        max_depth = 1

        while dq:
            node, level = dq.popleft()
            max_depth = max(max_depth, level)

            if node.left:
                dq.append([node.left, level + 1])
            if node.right:
                dq.append([node.right, level + 1])

        return max_depth
