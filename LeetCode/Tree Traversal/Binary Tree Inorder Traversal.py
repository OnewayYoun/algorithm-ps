from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            answer.append(node.val)
            inorder(node.right)

        inorder(root)
        return answer

    # iterative
    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            answer.append(current.val)
            current = current.right

        return answer
