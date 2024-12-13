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


print(Solution().combinationSum(candidates=[2, 3, 6, 7], target=7))
