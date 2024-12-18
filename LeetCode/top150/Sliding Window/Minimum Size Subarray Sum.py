from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_length = float('inf')
        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if min_length == float('inf') else min_length


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    output = 2

    print(output == Solution().minSubArrayLen(target, nums))