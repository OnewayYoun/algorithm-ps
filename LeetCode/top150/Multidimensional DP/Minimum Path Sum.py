from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        rows, cols = len(grid) - 1, len(grid[0]) - 1

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            if r == 0 and c == 0:
                return grid[0][0]
            if r == 0:
                dp[(r, c)] = grid[r][c] + dfs(r, c - 1)
                return dp[(r, c)]
            if c == 0:
                dp[(r, c)] = grid[r][c] + dfs(r - 1, c)
                return dp[(r, c)]

            dp[(r, c)] = min(grid[r][c] + dfs(r - 1, c), grid[r][c] + dfs(r, c - 1))
            return dp[(r, c)]

        return dfs(rows, cols)


class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]

        # 첫 번째 행
        for c in range(1, cols):
            dp[0][c] = dp[0][c - 1] + grid[0][c]

        # 첫 번째 열
        for r in range(1, rows):
            dp[r][0] = dp[r - 1][0] + grid[r][0]

        # 나머지
        for r in range(1, rows):
            for c in range(1, cols):
                dp[r][c] = grid[r][c] + min(
                    dp[r - 1][c],
                    dp[r][c - 1]
                )

        return dp[rows - 1][cols - 1]


print(Solution().minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
# print(Solution2().minPathSum([[1, 2, 3], [4, 5, 6]]))
