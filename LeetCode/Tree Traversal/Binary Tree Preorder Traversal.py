from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def preorder(node):
            if not node:
                return
            answer.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return answer

    # iterative
    def preorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                answer.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return answer
