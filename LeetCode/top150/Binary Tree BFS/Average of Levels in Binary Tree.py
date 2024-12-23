from collections import defaultdict, deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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
