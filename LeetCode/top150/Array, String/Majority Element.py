from typing import List
from collections import Counter, defaultdict


class Solution:
    """
    Input: nums = [3,2,3]
    Output: 3

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
    """

    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        dd = defaultdict(int)
        for i in nums:
            dd[i] += 1
        return sorted(dd.items(), key=lambda x: x[1], reverse=True)[0][0]


class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


class Solution4:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]

    def majorityElement1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        mid = len(nums) // 2
        L = self.majorityElement(nums[:mid])
        R = self.majorityElement(nums[mid:])

        return [R, L][nums.count(L) > mid]

    tmp = [(2,5), (3,4)]

print(Solution4().majorityElement([6, 5, 5]))
print(Solution4().majorityElement1([6, 5, 5]))
