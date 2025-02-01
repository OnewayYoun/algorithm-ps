from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]

    Input: preorder = [-1], inorder = [-1]
    Output: [-1]
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return

        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])

        return root

    # optimized version
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        cache = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx = 0

        def helper(left, right):
            nonlocal preorder_idx

            if left > right:
                return

            root = TreeNode(preorder[preorder_idx])
            preorder_idx += 1

            root_idx = cache[root.val]
            root.left = helper(left, root_idx - 1)
            root.right = helper(root_idx + 1, right)

            return root

        return helper(0, len(inorder) - 1)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().buildTree1(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))
