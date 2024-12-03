from typing import List
from itertools import combinations


class Solution:
    """
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Input: nums = [3,3], target = 6
    Output: [0,1]
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for (idx1, num1), (idx2, num2) in combinations(enumerate(nums), 2):
            if num1 + num2 == target:
                return [idx1, idx2]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, val in enumerate(nums):
            if target - val in d:
                return [idx, d[target - val]]
            d[val] = idx

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
        left, right = 0, len(nums) - 1
        while left != right:
            if sorted_nums[left][1] + sorted_nums[right][1] > target:
                right -= 1
            elif sorted_nums[left][1] + sorted_nums[right][1] < target:
                left += 1
            else:
                return [sorted_nums[left][0], sorted_nums[right][0]]


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum2([2, 7, 11, 15], 9))
print(Solution().twoSum3([2, 7, 11, 15], 9))
