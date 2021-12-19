from itertools import combinations
from typing import List


class Solution:
    # O(n^2)
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        indices = [i for i in range(len(nums))]

        for i1, i2 in combinations(indices, 2):
            if nums[i1] + nums[i2] == target:
                return [i1, i2]

    # O(n)
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[target-nums[i]] = i


if __name__ == '__main__':
    a = Solution()
    print(a.twoSum1(nums=[2, 7, 11, 15], target=9))
    print(a.twoSum2(nums=[2, 7, 11, 15], target=9))