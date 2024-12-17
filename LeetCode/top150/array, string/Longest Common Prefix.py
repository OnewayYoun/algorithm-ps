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

    def longestCommonPrefix1(self, strs: List[str]) -> str:
        prefix = strs[0]
        n = len(prefix)

        for i in range(1, len(strs)):
            while prefix != strs[i][:n]:
                n -= 1
                if n == 0:
                    return ''
                prefix = prefix[:n]
        return prefix


print(Solution().longestCommonPrefix(["flower"]))
print(Solution().longestCommonPrefix1(["flower"]))
