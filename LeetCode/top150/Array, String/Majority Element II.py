from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        L = self.majorityElement(nums[:mid])
        R = self.majorityElement(nums[mid:])

        s = set(L + R)

        answer = []
        for num in s:
            if nums.count(num) > len(nums) // 3:
                answer.append(num)
        return answer


print(Solution().majorityElement(nums=[1, 2, 1, 2]))