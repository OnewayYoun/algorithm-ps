class Solution:
    """
    Input: num = 3749
    Output: "MMMDCCXLIX"


    Input: num = 58
    Output: "LVIII"

    Input: num = 1994
    Output: "MCMXCIV"
    """

    def intToRoman(self, num: int) -> str:
        symbols = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

        answer = ''
        thousands = (num // 1000) % 10
        hundreds = (num // 100) % 10
        tens = (num // 10) % 10
        ones = (num // 1) % 10

        if thousands != 0:
            answer += symbols[1000] * thousands
        if hundreds != 0:
            if 0 < hundreds < 4:
                answer += symbols[100] * hundreds
            elif hundreds == 4:
                answer += symbols[100] + symbols[500]
            elif 5 <= hundreds < 9:
                answer += symbols[500] + symbols[100] * (hundreds % 5)
            elif hundreds == 9:
                answer += symbols[100] + symbols[1000]
        if tens != 0:
            if 0 < tens < 4:
                answer += symbols[10] * tens
            elif tens == 4:
                answer += symbols[10] + symbols[50]
            elif 5 <= tens < 9:
                answer += symbols[50] + symbols[10] * (tens % 5)
            elif tens == 9:
                answer += symbols[10] + symbols[100]
        if ones != 0:
            if 0 < ones < 4:
                answer += symbols[1] * ones
            elif ones == 4:
                answer += symbols[1] + symbols[5]
            elif 5 <= ones < 9:
                answer += symbols[5] + symbols[1] * (ones % 5)
            elif ones == 9:
                answer += symbols[1] + symbols[10]

        return answer

    def intToRoman2(self, num: int) -> str:
        symbols = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        answer = ''
        for key, val in reversed(symbols.items()):
            cnt = num // key
            num -= cnt * key
            answer += cnt * val
            if num == 0:
                break
        return answer


print(Solution().intToRoman(3749))
print(Solution().intToRoman2(3749))
