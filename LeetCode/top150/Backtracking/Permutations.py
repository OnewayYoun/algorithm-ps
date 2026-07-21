from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        cur_lst = []
        visited = [False] * len(nums)

        def dfs():
            if len(cur_lst) == len(nums):
                answer.append(cur_lst[:])
                return

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    cur_lst.append(nums[i])

                    dfs()

                    visited[i] = False
                    cur_lst.pop()

        dfs()

        return answer


if __name__ == "__main__":
    print(Solution().permute(nums = [1,2,3]))