class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left, right = 0, len(s) - 1
        for i in t:
            if left > right:
                break
            if i == s[left]:
                left += 1
        return True if left > right else False


if __name__ == '__main__':
    # s = "abc"
    # t = "ahbgdc"

    s = "axc"
    t = "ahbgdc"

    print(Solution().isSubsequence(s, t))
