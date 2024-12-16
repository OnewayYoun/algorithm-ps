from typing import List


class Solution:
    """
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

    Input: strs = ["dog","racecar","car"]
    Output: ""
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        strs.sort()
        first, last = strs[0], strs[-1]
        n = min(len(first), len(last))

        for i in range(n):
            if first[i] == last[i]:
                prefix += first[i]
            else:
                return prefix
        return prefix


print(Solution().longestCommonPrefix(["flower"]))
