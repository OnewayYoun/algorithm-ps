class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''.join([str for str in s.lower() if str.isalnum()])
        return new_str == new_str[::-1]


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
