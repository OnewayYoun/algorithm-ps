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


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    answer = True
    print(answer == Solution().isPalindrome(s))