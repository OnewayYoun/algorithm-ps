from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        dq = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    dq.append((row, col, 0))

        answer = 0
        while dq:
            r, c, cnt = dq.popleft()
            answer = cnt
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_col = c + dx
                new_row = r + dy
                if new_col >= 0 and new_col != len(grid[0]) and new_row >= 0 and new_row != len(grid):
                    if grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        dq.append((new_row, new_col, cnt + 1))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
        return answer


print(Solution().orangesRotting(grid=[[2, 1, 1],
                                      [1, 1, 0],
                                      [0, 1, 1]]))

print(Solution().orangesRotting(grid=[[2, 1, 1],
                                      [0, 1, 1],
                                      [1, 0, 1]]))
