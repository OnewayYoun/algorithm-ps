from collections import defaultdict


class Solution:
    """
    Input: s = "egg", t = "add"
    Output: true

    Input: s = "foo", t = "bar"
    Output: false

    Input: s = "paper", t = "title"
    Output: true
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        match = {}
        added = set()

        for i in range(len(s)):
            if s[i] in match:
                continue
            if t[i] in added:
                return False
            match[s[i]] = t[i]
            added.add(t[i])

        tmp = ''
        for char in s:
            tmp += match[char]

        return tmp == t

    def isIsomorphic1(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


# print(Solution().isIsomorphic(s="badc", t="baba"))
print(Solution().isIsomorphic1(s="badc", t="baba"))
