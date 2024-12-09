from typing import List


class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        left = 0
        min_val = float('inf')

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_val = min(min_val, right + 1 - left)
                total -= nums[left]
                left += 1
        return min_val if min_val != float('inf') else 0


print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
