class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        s="abc", t="ahbgdc"
        s="axc", t="ahbgdc"
        """
        left, right = 0, len(s) - 1
        for i in t:
            if left > right:
                break
            if i == s[left]:
                left += 1
        return left > right


print(Solution().isSubsequence(s="abc", t="ahbgcdc"))
