from typing import List
from functools import lru_cache


class Solution:
    """
    Input: nums = [2,3,1,1,4]
    Output: true

    Input: nums = [3,2,1,0,4]
    Output: false
    """

    def canJump(self, nums: List[int]) -> bool:
        cur_idx = 0
        n = len(nums) - 1
        steps = nums[cur_idx]
        if n < 1:
            return True
        while steps:
            if steps + cur_idx >= n:
                return True
            steps -= 1
            cur_idx += 1
            if nums[cur_idx] > steps:
                steps = nums[cur_idx]
        return False

    def canJump1(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(goal, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False

    def canJump2(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {n - 1: True}

        def dp(i):
            if i in memo:
                return memo[i]

            for jump in range(1, nums[i] + 1):
                if dp(i + jump):
                    memo[i] = True
                    return memo[i]
            memo[i] = False
            return memo[i]

        return dp(0)

    def canJump3(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(None)
        def dp(i):
            if i == n - 1:
                return True
            for jump in range(1, nums[i] + 1):
                if dp(i + jump):
                    return True
            return False

        return dp(0)


# print(Solution().canJump([0, 1]))
# print(Solution().canJump1([3, 5, 1, 0, 4]))
print(Solution().canJump3([3, 5, 1, 0, 4]))
