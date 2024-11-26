from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        Input: s = ["h","e","l","l","o"]
        Output: ["o","l","l","e","h"]
        """

        """
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
        return s
        """

        """
        s.reverse()
        return s
        """

        """
        s[:] = s[::-1]
        return s
        """

        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


print(Solution().reverseString(["h", "e", "l", "l", "o"]))
