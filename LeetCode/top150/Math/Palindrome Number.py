import math


class Solution:
    """
    Input: x = 121
    Output: true

    Input: x = -121
    Output: false

    Input: x = 10
    Output: false
    """

    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def isPalindrome1(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True

        left, right = math.trunc(math.log(x, 10)), 0
        while left > right:
            if (x // (10 ** left)) % 10 != (x // (10 ** right)) % 10:
                return False
            left -= 1
            right += 1
        return True


# print(Solution().isPalindrome(121))
print(Solution().isPalindrome1(121))
