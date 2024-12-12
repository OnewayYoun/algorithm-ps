from typing import List
from collections import deque
from pprint import pprint


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def convert_position(number: int):
            r = n - 1 - (number - 1) // n
            c = (number - 1) % n
            if n % 2 == 0:
                if r % 2 == 0:
                    c = n - (number - 1) % n - 1
            else:
                if r % 2 == 1:
                    c = n - (number - 1) % n - 1
            return [r, c]

        n = len(board)
        visited = set()
        dq = deque([[1, 0]])
        while dq:
            cur, step = dq.popleft()
            for i in range(1, 7):
                next = cur + i
                r, c = convert_position(next)
                if board[r][c] != -1:
                    next = board[r][c]
                if next == n ** 2:
                    return step + 1
                if next not in visited:
                    dq.append([next, step + 1])
                    visited.add(next)
        return -1


print(Solution().snakesAndLadders(
    [[1, 1, -1],
     [1, 1, 1],
     [-1, 1, 1]])
)
