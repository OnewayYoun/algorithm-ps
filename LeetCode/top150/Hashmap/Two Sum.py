from typing import List


class Solution:
    """
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Input: nums = [3,3], target = 6
    Output: [0,1]
    """

    # for loop
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # two pointer & sort
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
        print(sorted_nums)
        left, right = 0, len(sorted_nums) - 1

        while left < right:
            if sorted_nums[left][1] + sorted_nums[right][1] < target:
                left += 1
            elif sorted_nums[left][1] + sorted_nums[right][1] > target:
                right -= 1
            else:
                return [sorted_nums[left][0], sorted_nums[right][0]]

    # dict
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, val in enumerate(nums):
            if val in d:
                return [d[val], idx]
            d[target - val] = idx

    # backtracking
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        answer = []

        def dfs(idx, cur, total):
            if len(cur) == 2 and total == target:
                answer.append(cur[:])
                return
            if len(cur) >= 2 or idx >= len(nums):
                return

            for i in range(idx, len(nums)):
                cur.append(i)
                dfs(i + 1, cur, total + nums[i])
                cur.pop()

        dfs(0, [], 0)
        return answer[0] if answer else []

    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        from itertools import combinations

        for comb in combinations(enumerate(nums), 2):
            if comb[0][1] + comb[1][1] == target:
                return [comb[0][0], comb[1][0]]


# print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
# print(Solution().twoSum1(nums=[2, 7, 11, 15], target=9))
# print(Solution().twoSum2(nums=[7, 2, 11, 15], target=9))
# print(Solution().twoSum3(nums=[0, 4, 3, 0], target=0))
print(Solution().twoSum4(nums=[7, 2, 11, 15], target=9))
