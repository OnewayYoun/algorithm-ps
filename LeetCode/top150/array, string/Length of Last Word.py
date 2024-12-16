import re

class Solution:
    """
    Input: s = "Hello World"
    Output: 5

    Input: s = "   fly me   to   the moon  "
    Output: 4

    Input: s = "luffy is still joyboy"
    Output: 6
    """

    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])


print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
