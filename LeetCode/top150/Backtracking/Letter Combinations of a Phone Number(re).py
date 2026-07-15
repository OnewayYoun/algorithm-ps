from typing import List


class Solution:
    digit_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        answer = []

        def dfs(idx, cur_str):
            if len(cur_str) == len(digits):
                answer.append(cur_str)
                return
            for char in self.digit_map[digits[idx]]:
                dfs(idx + 1, cur_str + char)
                print('hi')

        dfs(0, '')
        return answer


    def letterCombinations1(self, digits: str) -> List[str]:
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        answer = []
        cur = []

        def DFS(idx):
            if len(cur) == len(digits):
                answer.append(''.join(cur))
                return

            for char in d[digits[idx]]:
                cur.append(char)
                DFS(idx + 1)
                cur.pop()


        DFS(0)

        return answer


print(Solution().letterCombinations1("23"))
