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

    def isSubsequence1(self, s: str, t: str) -> bool:
        idx = 0

        for char in t:
            if idx == len(s):
                return True
            if char == s[idx]:
                idx += 1
        return idx == len(s)


print(Solution().isSubsequence(s="abc", t="ahbgcdc"))
print(Solution().isSubsequence1(s="abc", t="ahbgcdc"))
