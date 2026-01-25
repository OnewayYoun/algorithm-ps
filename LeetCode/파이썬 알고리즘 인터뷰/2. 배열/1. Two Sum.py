from typing import List


class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums: List[int], target: int) -> List[List[int]]:

        def combination():
            result = []

            def backtracking(start, path):
                if len(path) == 2:
                    if nums[path[0]] + nums[path[1]] == target:
                        result.append(path[:])
                    return

                for idx in range(start, len(nums)):
                    path.append(idx)
                    backtracking(idx + 1, path)
                    path.pop()

            backtracking(0, [])
            return result

        return combination()[0]

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        search = {v: i for i, v in enumerate(nums)}
        for i, v in enumerate(nums):
            if target - v in search and search[target - v] != i:
                return [i, search[target - v]]

    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        search = {}
        for i, v in enumerate(nums):
            if target - v in search:
                return [i, search[target - v]]
            search[v] = i

    def twoSum5(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
        left, right = 0, len(sorted_nums) - 1

        while left != right:
            if sorted_nums[left][1] + sorted_nums[right][1] == target:
                return [sorted_nums[left][0], sorted_nums[right][0]]
            elif sorted_nums[left][1] + sorted_nums[right][1] < target:
                left += 1
            else:
                right -= 1


if __name__ == "__main__":
    print(Solution().twoSum5(nums=[2, 7, 11, 15], target=9))
