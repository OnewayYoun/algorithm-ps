from typing import List


class Solution:
    """
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]

    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

    Input: candidates = [2], target = 1
    Output: []

    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(idx, cur, total):
            if total == target:
                answer.append(cur[:])
                return
            if total > target or idx >= len(candidates):
                return

            cur.append(candidates[idx])
            dfs(idx, cur, total + candidates[idx])
            cur.pop()
            dfs(idx + 1, cur, total)

        dfs(0, [], 0)
        return answer


print(Solution().combinationSum(candidates=[2, 4], target=5))
