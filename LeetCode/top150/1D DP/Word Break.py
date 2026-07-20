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

    def wordBreak_bottom_up(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]

    def wordBreak_top_down(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return True

            if start in memo:
                return memo[start]

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    if dfs(end):
                        memo[start] = True
                        return True
            memo[start] = False
            return False

        return dfs(0)


print(Solution().wordBreak_bottom_up(s = "leetcode", wordDict = ["lee", "leet", "tc", "ode", "code"]))
