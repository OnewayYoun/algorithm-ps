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























    def maxDepth_dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth_dfs(root.left), self.maxDepth_dfs(root.right))

    def maxDepth_dfs_iterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 1
        stack = [[root, level]]

        while stack:
            node, cur_level = stack.pop()
            if node:
                level = max(level, cur_level)
                stack.append([node.left, cur_level + 1])
                stack.append([node.right, cur_level + 1])
        return level

    def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
        level = 0
        if not root:
            return level

        dq = deque([root])
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            level += 1
        return level







if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Solution().maxDepth_dfs_iterative(root))
