from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(total: int, cur: List[int], idx: int):
            if total == target:
                answer.append(cur[:])
                return
            if total > target or idx >= len(candidates):
                return

            cur.append(candidates[idx])
            dfs(total + candidates[idx], cur, idx)
            cur.pop()
            dfs(total, cur, idx + 1)

        dfs(0, [], 0)

        return answer





























    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        cur_lst = []
        cur_sum = 0

        def dfs(idx):
            nonlocal cur_sum

            if idx == len(candidates):
                return

            if cur_sum == target:
                answer.append(cur_lst[:])
                return

            if cur_sum > target:
                return


            cur_lst.append(candidates[idx])
            cur_sum += candidates[idx]

            dfs(idx)

            cur_lst.pop()
            cur_sum -= candidates[idx]

            dfs(idx + 1)


        dfs(0)

        return answer

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        cur_lst = []

        def dfs(idx, cur_sum):
            if cur_sum == target:
                answer.append(cur_lst[:])
                return

            if cur_sum > target:
                return

            for i in range(idx, len(candidates)):
                cur_lst.append(candidates[i])
                dfs(i, cur_sum + candidates[i])
                cur_lst.pop()

        dfs(0, 0)

        return answer

print(Solution().combinationSum2(candidates=[1, 3, 6, 7], target=7))
