from typing import List


class Solution:
    """
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6

    Input: height = [4,2,0,3,2,5]
    Output: 9
    1 0 1
    """

    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left != right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max <= right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1
        return water


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
