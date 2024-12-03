class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        n = len(s)
        answer = ''
        max_length = 0
        for i in range(n):
            left, right = i, i
            cur_length = 1
            for _ in range(n // 2 + 1):
                if left >= 0 and right < n and s[left:right + 1] == s[left:right + 1][::-1]:
                    if cur_length > max_length:
                        max_length = cur_length
                        answer = s[left:right + 1]
                    left -= 1
                    right += 1
                    cur_length += 2
                else:
                    break

            left, right = i, i + 1
            cur_length = 2
            for _ in range(n // 2):
                if left >= 0 and right < n and s[left:right + 1] == s[left:right + 1][::-1]:
                    if cur_length > max_length:
                        max_length = cur_length
                        answer = s[left:right + 1]
                    left -= 1
                    right += 1
                    cur_length += 2
                else:
                    break
        return answer


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        n = len(s)
        start, size = 0, 1
        for i in range(1, n):
            l, r = i - size, i + 1
            s1, s2 = s[l - 1: r], s[l: r]

            if s1 == s1[::-1] and l - 1 >= 0:
                start, size = l - 1, size + 2
            elif s2 == s2[::-1]:
                start, size = l, size + 1
        return s[start:start + size]


class Solution3:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left:right + 1] == s[left:right + 1][::-1]:
                left -= 1
                right += 1
            return s[left + 1:right]

        answer = ''
        for i in range(len(s)):
            answer = max(answer, expand(i, i), expand(i, i + 1), key=len)

        return answer


print(Solution3().longestPalindrome("baaaaa"))