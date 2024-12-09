from typing import List


class Solution:
    """
    Input: nums = [1,4,3,2]
    Output: 4

    Input: nums = [6,2,6,5,1,2]
    Output: 9
    """

    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

    def arrayPairSum1(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        for i in range(0, len(nums), 2):
            total += nums[i]
        return total


print(Solution().arrayPairSum([6, 2, 6, 5, 1, 2]))
print(Solution().arrayPairSum1([6, 2, 6, 5, 1, 2]))
