from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        visited = set()

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return
            if (row, col) in visited or not grid[row][col]:
                return

            visited.add((row, col))
            for i in range(4):
                new_x, new_y = col + dx[i], row + dy[i]
                dfs(new_y, new_x)

        def bfs():
            cnt, dq = 0, deque(visited)

            while dq:
                for _ in range(len(dq)):
                    row, col = dq.popleft()
                    for i in range(4):
                        new_x, new_y = col + dx[i], row + dy[i]
                        if new_y < 0 or new_y >= len(grid) or new_x < 0 or new_x >= len(grid[0]):
                            continue
                        if (new_y, new_x) in visited:
                            continue
                        if grid[new_y][new_x]:
                            return cnt
                        if not grid[new_y][new_x]:
                            dq.append((new_y, new_x))
                            visited.add((new_y, new_x))
                cnt += 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()


grid = [[1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]]
print(Solution().shortestBridge(grid))
