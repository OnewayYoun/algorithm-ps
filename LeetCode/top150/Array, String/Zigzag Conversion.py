from collections import defaultdict


class Solution:
    """
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    P     I    N
    A   L S  I G
    Y A   H R
    P     I

    Input: s = "A", numRows = 1
    Output: "A"
    """

    def convert(self, s: str, numRows: int) -> str:
        answer = [[] for _ in range(numRows)]
        n = len(s)
        cur_dir = 'Down'
        idx = 0
        cur_row = 0
        while idx < n:
            answer[cur_row].append(s[idx])
            if cur_dir == 'Down':
                if 0 <= cur_row + 1 < numRows:
                    cur_row += 1
                else:
                    cur_row -= 1
                    cur_dir = 'Up'
            elif cur_dir == 'Up':
                if 0 <= cur_row - 1 < numRows:
                    cur_row -= 1
                else:
                    cur_row += 1
                    cur_dir = 'Down'
            idx += 1
        return ''.join(map(''.join, answer))

    # optimized version
    def convert1(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        answer = [[] for _ in range(numRows)]
        cur_direction = -1  # 1: down, -1: up
        cur_idx = 0

        for char in s:
            if cur_idx in (0, numRows - 1):  # change direction when the cur_idx in the boarder
                cur_direction *= -1
            answer[cur_idx].append(char)
            cur_idx += cur_direction

        return ''.join(map(''.join, answer))

    def convert2(self, s: str, numRows: int) -> str:
        cur = 1
        direction = -1
        dd = defaultdict(list)

        for char in s:
            dd[cur].append(char)
            if cur == 1 or cur == numRows:
                direction *= -1

            cur += direction

        return ''.join([''.join(val) for val in dd.values()])

    def convert3(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = []
        cycle = 2 * (numRows - 1)

        for row in range(numRows):
            for i in range(row, len(s), cycle):
                res.append(s[i])
                diagonal_idx = i + cycle - 2 * row
                if row not in (0, numRows - 1) and diagonal_idx < len(s):
                    res.append(s[diagonal_idx])

        return "".join(res)



print(Solution().convert3("PAYPALISHIRING", numRows=4))
# print(Solution().convert3("PAYPALISHIRING", numRows=4))
# Output: "PINALSIGYAHRPI"
# Output: "PINALSIGYAHPI"