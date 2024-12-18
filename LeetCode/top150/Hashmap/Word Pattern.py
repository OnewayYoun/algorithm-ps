from collections import defaultdict


class Solution:
    """
    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true

    Input: pattern = "abba", s = "dog cat cat fish"
    Output: false

    Input: pattern = "aaaa", s = "dog cat cat dog"
    Output: false
    """

    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        return len(set(zip(pattern, s))) == len(set(pattern)) == len(set(s))


print(Solution().wordPattern(pattern="abba", s="dog cat cat dog"))
