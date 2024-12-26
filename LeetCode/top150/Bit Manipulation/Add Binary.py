class Solution:
    """
    Input: a = "11", b = "1"
    Output: "100"

    Input: a = "1010", b = "1011"
    Output: "10101"
    """

    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), 'b')

    def addBinary1(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary2(self, a: str, b: str) -> str:
        answer = ''
        a, b = a[::-1], b[::-1]
        flag = 0

        for i in range(max(len(a), len(b))):
            digit_a = a[i] if i < len(a) else 0
            digit_b = b[i] if i < len(b) else 0

            added = int(digit_a) + int(digit_b) + flag
            answer = str(added % 2) + answer
            if added >= 2:
                flag = 1
            else:
                flag = 0
        return answer if flag == 0 else '1' + answer


print(Solution().addBinary(a="11", b="1"))
print(Solution().addBinary1(a="11", b="1"))
print(Solution().addBinary2(a="11", b="1"))
