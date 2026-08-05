# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        answer = None

        def dfs(node):
            nonlocal cnt, answer

            if answer is not None:
                return answer

            if not node:
                return

            dfs(node.left)
            cnt += 1
            if k == cnt:
                answer = node.val
            dfs(node.right)

        dfs(root)

        return answer