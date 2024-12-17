from collections import Counter


class Solution:
    """
    Input: s = "anagram", t = "nagaram"
    Output: true

    Input: s = "rat", t = "car"
    Output: false
    """

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram1(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


print(Solution().isAnagram(s="anagram", t="nagaram"))
