from typing import List


class Solution:
    """
    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or grid[y][x] == '0':
                return False
            else:
                grid[y][x] = '0'
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)
                return True

        cnt = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if dfs(col, row):
                    cnt += 1

        return cnt


















    def numIslands1(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def DFS(row, col):
            if row <= -1 or row >= rows or col <= -1 or col >= cols:
                return False

            if grid[row][col] == '1' and not visited[row][col]:
                visited[row][col] = True
                DFS(row + 1, col)
                DFS(row - 1, col)
                DFS(row, col + 1)
                DFS(row, col - 1)
                return True

            return False

        cnt = 0
        for r in range(rows):
            for c in range(cols):
                if DFS(r, c):
                    cnt += 1

        return cnt

print(Solution().numIslands1(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
