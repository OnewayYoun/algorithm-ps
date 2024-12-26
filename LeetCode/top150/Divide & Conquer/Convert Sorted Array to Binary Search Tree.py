from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted

    Input: nums = [1,3]
    Output: [3,1]
    Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
    """

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            return root

        return helper(0, len(nums) - 1)

    def sortedArrayToBST1(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        m = len(nums) // 2
        root = TreeNode(nums[m])
        root.left = self.sortedArrayToBST1(nums[:m])
        root.right = self.sortedArrayToBST1(nums[m + 1:])
        return root


print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))
print(Solution().sortedArrayToBST1([-10, -3, 0, 5, 9]))
