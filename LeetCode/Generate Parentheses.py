from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def dfs(num_open, num_close, cur_str):
            if num_open > n or num_close > num_open:
                return
            if len(cur_str) == n * 2:
                answer.append(cur_str)
                return
            dfs(num_open + 1, num_close, cur_str + '(')
            dfs(num_open, num_close + 1, cur_str + ')')

        dfs(0, 0, '')

        return answer

    # optimized version
    def generateParenthesis1(self, n: int) -> List[str]:
        answer = []

        def dfs(num_open, num_close, cur):
            if num_open > n or num_close > num_open:
                return
            if len(cur) == n * 2:
                answer.append(''.join(cur))
                return
            cur.append('(')
            dfs(num_open + 1, num_close, cur)
            cur.pop()

            cur.append(')')
            dfs(num_open, num_close + 1, cur)
            cur.pop()

        dfs(0, 0, [])

        return answer


print(Solution().generateParenthesis1(3))
