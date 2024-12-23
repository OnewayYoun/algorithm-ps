from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        answer = []
        dq = deque()
        dq.append(root)

        while dq:
            n = len(dq)
            tmp = []

            for _ in range(n):
                node = dq.popleft()
                tmp.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            answer.append(tmp)
        return answer

    # DFS
    def levelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, level):
            if not node:
                return
            if level == len(answer):
                answer.append([])
            answer[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        answer = []
        dfs(root, 0)

        return answer
