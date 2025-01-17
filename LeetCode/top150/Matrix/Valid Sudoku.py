from typing import List
from collections import defaultdict


class Solution:
    """
    Input: board =
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: true

    Input: board =
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: false
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validate_rows(board):
            for row in board:
                tmp_set = set()
                for char in row:
                    if char != '.' and char not in tmp_set:
                        tmp_set.add(char)
                    elif char != '.' and char in tmp_set:
                        return False
            return True

        def validate_columns(board):
            for column in zip(*board):
                tmp_set = set()
                for char in column:
                    if char != '.' and char not in tmp_set:
                        tmp_set.add(char)
                    elif char != '.' and char in tmp_set:
                        return False
            return True

        def validate_3x3_grid(board):
            boxes = []
            for row_start in range(0, 9, 3):
                for col_start in range(0, 9, 3):
                    tmp = []
                    for row in range(row_start, row_start + 3):
                        tmp += board[row][col_start:col_start + 3]
                    boxes.append(tmp)
            return validate_rows(boxes)

        return validate_3x3_grid(board) and validate_rows(board) and validate_columns(board)

    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        columns = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in boxes[str(r // 3) + str(c // 3)]:
                    return False
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                boxes[str(r // 3) + str(c // 3)].add(board[r][c])
        return True


print(Solution().isValidSudoku1(board=
                                [["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
