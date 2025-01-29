from typing import List


class Solution:
    """
    Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

    Input: board = [["X"]]
    Output: [["X"]]
    """

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        tmp_list = []

        def dfs(y, x):
            if board[y][x] == 'X':
                return False
            if y in (0, len(board) - 1) or x in (0, len(board[0]) - 1):
                return True
            else:
                tmp_list.append((y, x))
                board[y][x] = 'X'
                is_touched = dfs(y + 1, x) or dfs(y - 1, x) or dfs(y, x + 1) or dfs(y, x - 1)
            return is_touched

        for row in range(1, len(board)):
            for col in range(1, len(board[0])):
                if not dfs(row, col):
                    tmp_list = []
                else:
                    while tmp_list:
                        y, x = tmp_list.pop()
                        board[y][x] = 'O'

        print(board)


print(Solution().solve(
    board=[
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]))
