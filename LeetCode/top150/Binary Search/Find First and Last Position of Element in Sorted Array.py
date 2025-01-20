from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    """
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

    Input: nums = [], target = 0
    Output: [-1,-1]
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        first_idx = bisect_left(nums, target)
        if first_idx < len(nums) and nums[first_idx] == target:
            return [first_idx, bisect_right(nums, target) - 1]
        else:
            return [-1, -1]

    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        def bl(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def br(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        first_idx = bl(left, right)
        if first_idx < len(nums) and nums[first_idx] == target:
            return [first_idx, br(left, right) - 1]
        else:
            return [-1, -1]


print(Solution().searchRange(nums=[2, 2], target=3))
