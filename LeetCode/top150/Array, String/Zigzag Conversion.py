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


print(Solution().convert("PAYPALISHIRING", numRows=4))
print(Solution().convert1("PAYPALISHIRING", numRows=4))
