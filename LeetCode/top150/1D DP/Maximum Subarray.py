from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)

    def maxSubArray1(self, nums: List[int]) -> int:
        current = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current = max(current + nums[i], nums[i])
            max_sum = max(max_sum, current)

        return max_sum


print(Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().maxSubArray1(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
