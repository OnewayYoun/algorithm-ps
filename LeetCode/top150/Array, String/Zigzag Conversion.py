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


print(Solution().convert("PAYPALISHIRING", numRows=4))
