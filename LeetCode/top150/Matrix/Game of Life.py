import copy
from itertools import product
from typing import List


class Solution:
    """
    Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

    Input: board = [[1,1],[1,0]]
    Output: [[1,1],[1,1]]

    """

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1)
        ]
        copied_board = copy.deepcopy(board)
        num_row, num_col = len(board), len(board[0])

        def count_live_and_dead(row, col):
            counts = [0, 0]
            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]
                if 0 <= new_row < num_row and 0 <= new_col < num_col:
                    counts[copied_board[new_row][new_col]] += 1
            return counts

        for row in range(num_row):
            for col in range(num_col):
                dead_cnt, live_cnt = count_live_and_dead(row, col)
                if copied_board[row][col] == 1:
                    if live_cnt < 2:
                        board[row][col] = 0
                    elif live_cnt == 2 or live_cnt == 3:
                        board[row][col] = 1
                    else:
                        board[row][col] = 0
                else:
                    if live_cnt == 3:
                        board[row][col] = 1

        print(board)


print(Solution().gameOfLife(board=[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
