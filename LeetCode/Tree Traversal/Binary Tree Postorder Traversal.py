from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            answer.append(node.val)

        postorder(root)
        return answer

    # iterative
    def postorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                answer.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return answer[::-1]
