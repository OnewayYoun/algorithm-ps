from typing import List


class Solution:
    """
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0

    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    """

    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1


print(Solution().strStr(haystack="sadbutsad", needle="sad"))
