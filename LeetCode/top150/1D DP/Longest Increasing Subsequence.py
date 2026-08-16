from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)


    def lengthOfLIS2(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

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

tmp = [1,2,3,4,5,6]
print(bisect_left(tmp, 5))
# print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
# print(Solution().lengthOfLIS2([10, 9, 2, 5, 3, 7, 101, 18]))
# print(Solution2().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
