from typing import List


class Solution:
    """
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49

    Input: height = [1,1]
    Output: 1
    """

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        n = len(height) - 1
        max_water = float('-inf')

        while left < right:
            max_water = max(max_water, min(height[left], height[right]) * n)
            n -= 1
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_water





















    def maxArea1(self, height: List[int]) -> int:
        max_area = float('-inf')
        left, right = 0, len(height) - 1

        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


print(Solution().maxArea1([1, 8, 6, 2, 5, 4, 8, 3, 7]))
# print(Solution().maxArea([1, 3, 2, 5, 25, 24, 5]))
