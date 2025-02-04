class Solution:
    """
    Input: s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

    Input: s = "Mr Ding"
    Output: "rM gniD"
    """

    def reverseWords(self, s: str) -> str:
        answer = []

        for word in s.split():
            answer.append(word[::-1])

        return ' '.join(answer)


print(Solution().reverseWords(s="Let's take LeetCode contest"))
