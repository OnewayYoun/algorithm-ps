class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i), expand(i, i + 1), key=len)

        return result


if __name__ == '__main__':
    print(Solution().longestPalindrome(s="babad"))
    # print(Solution().longestPalindrome(s="cbbd"))