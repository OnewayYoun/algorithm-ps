from typing import List


class Solution:
    """
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def find_zeros():
            zeros_row, zeros_col = set(), set()
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    if matrix[row][col] == 0:
                        zeros_row.add(row)
                        zeros_col.add(col)
            return zeros_row, zeros_col

        zeros_row, zeros_col = find_zeros()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in zeros_row or col in zeros_col:
                    matrix[row][col] = 0

    # saving space complexity to O(1)
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        zero_row = False

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        zero_row = True

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        if matrix[0][0] == 0:
            for row in range(len(matrix)):
                matrix[row][0] = 0

        if zero_row:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0


print(Solution().setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(Solution().setZeroes1(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
