from collections import defaultdict
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dd = defaultdict(int)
        for num in nums:
            dd[num] += 1

        idx = 0
        for i in range(3):
            for _ in range(dd[i]):
                nums[idx] = i
                idx += 1


    def sortColors1(self, nums: List[int]) -> None:
        left = 0
        cur = 0
        right = len(nums) - 1

        while cur <= right:
            if nums[cur] == 0:
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
            else:  # nums[cur] == 1
                cur += 1

Solution().sortColors1(nums=[2, 0, 1])
