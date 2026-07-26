from collections import defaultdict, Counter
from typing import List


class Solution:
    """
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Input: nums = [0,1,1]
    Output: []

    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_list = []
        for key, val in Counter(nums).items():
            if val >= 3:
                new_list = new_list + [key] * 3
            else:
                new_list = new_list + [key] * val

        answer = set()
        for idx, target in enumerate(new_list):
            dd = defaultdict()
            for i, val in enumerate(new_list):
                if i == idx:
                    continue
                if -target - val in dd:
                    answer.add(tuple(sorted([target, val, new_list[dd[-target - val]]])))
                dd[val] = i
        return list(map(list, answer))




















    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()

        for idx, val in enumerate(nums):
            dd = set()
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            for i in range(idx + 1, len(nums)):
                if -val - nums[i] in dd:
                    answer.add((val, nums[i], -val - nums[i]))
                dd.add(nums[i])

        return list(map(list, answer))

print(Solution().threeSum3([0, 0, 0, 0]))
