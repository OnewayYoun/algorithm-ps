from typing import List


class Solution:
    """
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true

    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: true

    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: false
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s) + 1):
            for word in wordDict:
                if dp[i] and s[i:i + len(word)] == word:
                    if i + len(word) == len(s) + 1:
                        return True
                    dp[i + len(word)] = True
        return dp[len(s)]


print(Solution().wordBreak(s="cars", wordDict=["car", "ca", "rs"]))
