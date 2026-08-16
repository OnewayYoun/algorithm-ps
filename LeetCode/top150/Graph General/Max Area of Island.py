from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return 0
            if grid[row][col] == 0:
                return 0

            if grid[row][col] == 1:
                grid[row][col] = 0

                return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        max_cnt = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                max_cnt = max(max_cnt, dfs(row, col))

        return max_cnt


grid = [[1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]]
print(Solution().maxAreaOfIsland(grid))
