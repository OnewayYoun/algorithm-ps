class Solution:
    """
    Input: s = "the sky is blue"
    Output: "blue is sky the"

    Input: s = "  hello world  "
    Output: "world hello"

    Input: s = "a good   example"
    Output: "example good a"
    """

    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


print(Solution().reverseWords(s="a good   example"))
