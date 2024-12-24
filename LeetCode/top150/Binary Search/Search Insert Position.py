from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    """
    Input: nums = [1,3,5,6], target = 5
    Output: 2

    Input: nums = [1,3,5,6], target = 2
    Output: 1

    Input: nums = [1,3,5,6], target = 7
    Output: 4
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)

    def searchInsert1(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (right + left) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return left


# print(Solution().searchInsert(nums=[1, 3, 5, 6], target=5))
print(Solution().searchInsert1(nums=[1, 3, 5, 6], target=0))
