import re


class Solution:
    """
    Input: s = "III"
    Output: 3

    Input: s = "LVIII"
    Output: 58

    Input: s = "MCMXCIV"
    Output: 1994

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    """

    def romanToInt(self, s: str) -> int:
        answer = 0
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        edge_cases = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        if len(s) == 1:
            return symbols[s]

        for key, val in edge_cases.items():
            while key in s:
                answer += val
                s = s.replace(key, "")

        for symbol in s:
            answer += symbols[symbol]

        return answer


print(Solution().romanToInt("MCMXCIV"))
