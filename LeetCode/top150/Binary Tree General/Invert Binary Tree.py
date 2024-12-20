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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)

        return root

    # BFS
    def invertTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque()
        dq.append(root)

        while dq:
            node = dq.popleft()
            if node:
                node.left, node.right = node.right, node.left
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return root
