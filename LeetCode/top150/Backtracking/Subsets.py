from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(idx, cur_lst):
            answer.append(cur_lst[:])

            for i in range(idx, len(nums)):
                cur_lst.append(nums[i])
                dfs(i + 1, cur_lst)
                cur_lst.pop()


        dfs(0, [])
        return answer


    def subsets1(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def dfs(idx, path):
            if idx == len(nums):
                answer.append(path[:])
                return

            path.append(nums[idx])
            dfs(idx + 1, path)
            path.pop()

            dfs(idx + 1, path)

        dfs(0, [])

        return answer

print(Solution().subsets1(nums=[1, 2, 3]))
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
