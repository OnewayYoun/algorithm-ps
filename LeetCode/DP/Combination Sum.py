from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(i, cur, total):
            if total == target:
                answer.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return answer


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))  # [[2,2,3],[7]]
