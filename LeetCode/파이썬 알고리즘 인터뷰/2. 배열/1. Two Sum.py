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


if __name__ == "__main__":
    print(Solution().twoSum3(nums=[2, 7, 11, 15], target=9))
