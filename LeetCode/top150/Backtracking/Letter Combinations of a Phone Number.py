from itertools import product
from typing import List


class Solution:
    """
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    Input: digits = ""
    Output: []

    Input: digits = "2"
    Output: ["a","b","c"]
    """

    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def dfs(idx, cur_string):
            if len(digits) == len(cur_string):
                answer.append(cur_string)
                return
            for char in digit_map[digits[idx]]:
                dfs(idx + 1, cur_string + char)

        if not digits:
            return []
        dfs(0, '')
        return answer

    def letterCombinations1(self, digits: str) -> List[str]:
        if not digits:
            return []

        answer = []
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        groups = [digit_map[d] for d in digits]
        for p in product(*groups):
            answer.append(''.join(p))

        return answer


print(Solution().letterCombinations1("23"))
