from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlatic = set(), set()

        def dfs(row, col, visited, prev_height):
            if (row, col) in visited or row < 0 or row >= len(heights) or col < 0 or col >= len(heights[0]):
                return
            if prev_height > heights[row][col]:
                return
            visited.add((row, col))
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])

        for r in range(len(heights)):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, len(heights[0]) - 1, atlatic, heights[r][len(heights[0]) - 1])

        for c in range(len(heights[0])):
            dfs(0, c, pacific, heights[0][c])
            dfs(len(heights) - 1, c, atlatic, heights[len(heights) - 1][c])

        return list(pacific.intersection(atlatic))


print(Solution().pacificAtlantic(heights=[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
