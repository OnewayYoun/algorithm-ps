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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        min_val = float('inf')

        def dfs(node):
            nonlocal prev, min_val
            if not node:
                return
            dfs(node.left)
            if prev:
                min_val = min(min_val, node.val - prev)
            prev = node
            dfs(node.right)

        dfs(root)
        return min_val

    # BFS
    def getMinimumDifference1(self, root: Optional[TreeNode]) -> int:
        stack, current = deque(), root
        prev = None
        min_val = float('inf')

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            node = stack.pop()
            if prev:
                min_val = min(min_val, node.val - prev.val)
            prev = node
            current = node.right
        return min_val
