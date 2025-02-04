class Solution:
    """
    Input: s = "abcdefg", k = 2
    Output: "bacdfeg"

    Input: s = "abcd", k = 2
    Output: "bacd"
    """

    def reverseStr(self, s: str, k: int) -> str:
        answer = []

        for i in range(0, len(s), k):
            if i % (2 * k) == 0:
                answer.append(s[i:i + k][::-1])
            else:
                answer.append(s[i:i + k])

        return ''.join(answer)


print(Solution().reverseStr(s="abcdefg", k=2))
