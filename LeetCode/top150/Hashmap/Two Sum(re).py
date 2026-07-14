from collections import defaultdict
from typing import List


class Solution:
    """
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Input: nums = [3,3], target = 6
    Output: [0,1]
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dd = defaultdict()

        for idx, num in enumerate(nums):
            if target - num in dd:
                return [dd[target - num], idx]
            dd[num] = idx


















    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for idx, num in enumerate(nums):
            if target - num in d:
                return [idx, d[target - num]]
            d[num] = idx
        return []

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        new_nums = [[num, idx] for idx, num in enumerate(nums)]
        new_nums.sort(key=lambda x: x[0])
        left, right = 0, len(nums) - 1

        while left < right:
            if new_nums[left][0] + new_nums[right][0] > target:
                right -= 1
            elif new_nums[left][0] + new_nums[right][0] < target:
                left += 1
            else:
                return [new_nums[left][1], new_nums[right][1]]


print(Solution().twoSum2([3, 2, 4], 6))
