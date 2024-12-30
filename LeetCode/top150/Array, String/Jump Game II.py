from collections import deque
from typing import List


class Solution:
    """
    Input: nums = [2,3,1,1,4]
    Output: 2

    Input: nums = [2,3,0,1,4]
    Output: 2
    """

    def jump(self, nums: List[int]) -> int:
        dq = deque()
        dq.append([0, 0])
        n = len(nums) - 1
        visited = set()

        while dq:
            cur_idx, steps = dq.popleft()
            if cur_idx == n:
                return steps
            for i in range(cur_idx, cur_idx + nums[cur_idx] + 1):
                if i not in visited:
                    dq.append([i, steps + 1])
                    visited.add(i)
        return -1

    def jump1(self, nums: List[int]) -> int:
        steps = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            steps += 1
        return steps

    def jump2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        dp = [0] * n
        j = 0
        for i in range(1, n):
            while j + nums[j] < i:
                j += 1
            dp[i] = dp[j] + 1

        return dp[-1]

    def jump3(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[-1]


print(Solution().jump3([2, 3, 1, 1, 4]))
