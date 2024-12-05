from typing import List
from itertools import combinations
from collections import Counter


class Solution:
    """
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Input: nums = [0,1,1]
    Output: []

    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    """

    # Time Limit Exceeded
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_list = []
        for key, val in Counter(nums).items():
            if val >= 3:
                new_list = new_list + [key] * 3
            else:
                new_list = new_list + [key] * val
        answer = set()
        for comb in combinations(new_list, 3):
            if sum(comb) == 0:
                answer.add(tuple(sorted(comb)))
        return list(map(list, answer))

    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        new_list = []
        for key, val in Counter(nums).items():
            if val >= 3:
                new_list = new_list + [key] * 3
            else:
                new_list = new_list + [key] * val
        answer = set()
        for idx, val in enumerate(new_list):
            d = {}
            for i in range(len(new_list)):
                if idx == i:
                    continue
                if -val - new_list[i] in d:
                    answer.add(tuple(sorted((val, new_list[i], -val - new_list[i]))))
                d[new_list[i]] = i
        return list(map(list, answer))

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        for idx, val in enumerate(nums):
            if idx != 0 and nums[idx-1] == val:
                continue
            left, right = idx + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < -val:
                    left += 1
                elif nums[left] + nums[right] > -val:
                    right -= 1
                else:
                    answer.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return answer


print(Solution().threeSum2([-1, 0, 1, 2, -1, -4]))
