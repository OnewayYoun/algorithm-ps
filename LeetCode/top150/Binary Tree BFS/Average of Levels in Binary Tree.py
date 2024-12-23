from collections import defaultdict, deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        dd = defaultdict(list)
        dq = deque()
        dq.append((root, 0))

        while dq:
            node, level = dq.popleft()
            dd[level].append(node.val)
            if node.left:
                dq.append((node.left, level + 1))
            if node.right:
                dq.append((node.right, level + 1))

        return [sum(val) / len(val) for _, val in sorted(dd.items())]

    # DFS
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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

        return [sum(i) / len(i) for i in answer]
