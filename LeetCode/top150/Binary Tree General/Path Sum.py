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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, total):
            if not node:
                return False

            cur_sum = total + node.val
            if not node.left and not node.right:
                return cur_sum == targetSum
            return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)

        return dfs(root, 0)

    # BFS
    def hasPathSum1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        dq = deque()
        dq.append([root, root.val])

        while dq:
            node, total = dq.popleft()
            if not node.left and not node.right:
                if total == targetSum:
                    return True
            if node.left:
                dq.append([node.left, total + node.left.val])
            if node.right:
                dq.append([node.right, total + node.right.val])
        return False
