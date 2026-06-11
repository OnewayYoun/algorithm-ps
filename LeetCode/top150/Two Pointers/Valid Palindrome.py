import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        left, right = 0, len(s) - 1
        if len(s) == 0:
            return True
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char for char in s.lower() if char.isalnum()]
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True



if __name__ == '__main__':
    s = "acc"
    print(Solution().isPalindrome(s))