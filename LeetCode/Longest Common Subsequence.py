class Solution:
    """
    Input: text1 = "abcde", text2 = "ace"
    Output: 3
    Explanation: The longest common subsequence is "ace" and its length is 3.

    Input: text1 = "abc", text2 = "abc"
    Output: 3
    Explanation: The longest common subsequence is "abc" and its length is 3.

    Input: text1 = "abc", text2 = "def"
    Output: 0
    Explanation: There is no such common subsequence, so the result is 0.
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def dfs(i: int, j: int) -> int:
            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))

            return cache[(i, j)]

        return dfs(0, 0)

    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        cache = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    cache[i][j] = 1 + cache[i + 1][j + 1]
                else:
                    cache[i][j] = max(cache[i + 1][j], cache[i][j + 1])

        return cache[0][0]


# print(Solution().longestCommonSubsequence(text1="abcde", text2="ace"))
print(Solution().longestCommonSubsequence1(text1="abcde", text2="ace"))
