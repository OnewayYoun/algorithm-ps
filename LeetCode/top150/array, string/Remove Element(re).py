from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        answer = len(nums)
        for idx, num in enumerate(nums):
            if num == val:
                nums[idx] = float('inf')
                answer -= 1
        nums.sort()
        print(nums)
        return answer


class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx


print(Solution().removeElement([3, 2, 2, 3], 3))
print(Solution2().removeElement([3, 2, 2, 3], 3))
