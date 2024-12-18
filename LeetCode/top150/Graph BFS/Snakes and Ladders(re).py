from typing import List
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()

        def get_coordinate(number: int):
            r = (number - 1) // n
            c = (number - 1) % n
            if r % 2 == 1:
                c = (n - 1) - c
            return [r, c]

        n = len(board)
        visited = set()

        def bfs(number: int, step):
            dq = deque()
            dq.append([number, step])

            while dq:
                number, step = dq.popleft()
                for i in range(1, 7):
                    new_num = number + i
                    row, col = get_coordinate(new_num)

                    if board[row][col] != -1:
                        new_num = board[row][col]
                    if new_num not in visited:
                        dq.append([new_num, step + 1])
                        visited.add(new_num)
                    if new_num == n ** 2:
                        return step + 1
            return -1

        return bfs(1, 0)


board = [[1, 1, -1],
         [1, 1, 1],
         [-1, 1, 1]]
print(Solution().snakesAndLadders(board))
