import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # words = ''.join([i for i in s.lower() if i.isalnum()])
        return words == words[::-1]

    def isPalindrome2(self, s: str) -> bool:
        s = ''.join([i for i in s.lower() if i.isalnum()])

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
