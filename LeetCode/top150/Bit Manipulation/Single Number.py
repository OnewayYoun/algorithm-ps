from typing import List


class Solution:
    """
    Input: nums = [2,2,1]
    Output: 1

    Input: nums = [4,1,2,1,2]
    Output: 4

    Input: nums = [1]
    Output: 1
    """

    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        tmp = nums[0]
        for i in range(2, len(nums), 2):
            if nums[i - 1] != tmp:
                return tmp
            tmp = nums[i]
        return tmp

    def singleNumber1(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer ^= num
        return answer


print(Solution().singleNumber(nums=[4, 1, 2, 1, 2]))
