from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(row, col):
            if grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            count = 1
            for r in range(rows):
                if grid[r][col] == 1:
                    count += dfs(r, col)
            for c in range(cols):
                if grid[row][c] == 1:
                    count += dfs(row, c)
            return count

        cnt = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                tmp_cnt = dfs(row, col)
                if tmp_cnt > 1:
                    cnt += tmp_cnt

        return cnt

grid = [[1,0,0,1,0],
        [0,0,0,0,0],
        [0,0,0,1,0]]
print(Solution().countServers(grid))
