class Solution:
    """
    Input: s = "babad"
    Output: "bab"

    Input: s = "cbbd"
    Output: "bb"
    """

    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        def helper(left, right):
            while left >= 0 and right < len(s) and s[left:right + 1] == s[left:right + 1][::-1]:
                left -= 1
                right += 1
            return s[left + 1:right]

        answer = ''
        for i in range(len(s)):
            answer = max(answer, helper(i, i), helper(i, i + 1), key=len)

        return answer


print(Solution().longestPalindrome(s="babad"))
