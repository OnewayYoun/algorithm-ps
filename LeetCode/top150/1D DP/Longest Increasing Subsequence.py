from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        answer = [nums[0]]
        for val in nums[1:]:
            if val > answer[-1]:
                answer.append(val)
            else:
                answer[bisect_left(answer, val)] = val
        return len(answer)


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(Solution2().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
