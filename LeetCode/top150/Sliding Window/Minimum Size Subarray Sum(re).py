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


















    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        cur_pointer = 0
        cur_sum = 0
        answer = float('inf')
        for i in range(len(nums)):
            cur_sum += nums[i]
            while cur_sum >= target:
                answer = min(answer, i - cur_pointer + 1)
                cur_sum -= nums[cur_pointer]
                cur_pointer += 1

        return answer if answer != float('inf') else 0


print(Solution().minSubArrayLen1(7, [2, 3, 1, 2, 4, 3]))
