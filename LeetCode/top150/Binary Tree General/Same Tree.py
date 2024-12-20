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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # BFS
    def isSameTree1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(root):
            result = []
            dq = deque([root])
            while dq:
                node = dq.popleft()
                if node:
                    result.append(node.val)
                    dq.append(node.left)
                    dq.append(node.right)
                else:
                    result.append(None)
            return result

        return bfs(p) == bfs(q)
