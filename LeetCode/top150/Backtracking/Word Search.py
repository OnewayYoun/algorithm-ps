from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        def dfs(x, y, idx):
            if idx == len(word):
                return True

            if not (0 <= x < len(board[0])) or not (0 <= y < len(board)) or board[y][x] != word[idx] or visited[y][x]:
                return False

            visited[y][x] = True

            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if dfs(new_x, new_y, idx + 1):
                    return True
            visited[y][x] = False

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(j, i, 0):
                    return True
        return False


print(Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))

"""
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
"""
