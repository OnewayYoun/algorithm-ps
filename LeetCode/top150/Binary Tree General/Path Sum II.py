# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum_bfs(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []

        if not root:
            return answer

        def bfs():
            dq = deque()
            dq.append((root, root.val, [root.val]))

            while dq:
                node, total_sum, path = dq.popleft()

                if not node.left and not node.right:
                    if total_sum == targetSum:
                        answer.append(path)

                if node.left:
                    left_path = path[:]
                    left_path.append(node.left.val)
                    dq.append((node.left, node.left.val + total_sum, left_path))
                if node.right:
                    right_path = path[:]
                    right_path.append(node.right.val)
                    dq.append((node.right, node.right.val + total_sum, right_path))

        bfs()
        return answer


    def pathSum_dfs(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []
        def dfs(node, total_sum, path):
            if not node:
                return

            cur_sum = total_sum + node.val
            path.append(node.val)

            if not node.left and not node.right:
                if cur_sum == targetSum:
                    answer.append(path[:])

            if node.left:
                dfs(node.left, cur_sum, path)
                path.pop()
            if node.right:
                dfs(node.right, cur_sum, path)
                path.pop()

        dfs(root, 0, [])

        return answer