'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m * n == 1:
            return 1
        if m * n == 0:
            return 0
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
'''


class Solution:
    def uniquePaths(self, m: int, n: int, dp={}) -> int:
        key = f'{m},{n}'
        if key in dp:
            return dp[key]
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        dp[key] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        return dp[key]


class Solution2:
    def uniquePaths(self, m: int, n: int, dp=None) -> int:
        if dp is None:
            dp = {}
        if (m, n) in dp:
            return dp[(m, n)]
        if m == 1 or n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        dp[(m, n)] = self.uniquePaths(m - 1, n, dp) + self.uniquePaths(m, n - 1, dp)
        return dp[(m, n)]


if __name__ == '__main__':
    print(Solution().uniquePaths(2, 3))
    print(Solution2().uniquePaths(2, 3))
