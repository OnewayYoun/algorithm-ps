from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[-1]

        dp = [0] * (len(nums) + 1)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 3] + nums[i])

        return max(dp)

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


if __name__ == "__main__":
    print(Solution().rob(nums=[2, 1, 1, 2]))
