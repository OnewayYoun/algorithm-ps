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


print(Solution().twoSum([2, 7, 11, 15], 9))
