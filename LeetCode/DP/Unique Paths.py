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
            return dp[f'{m},{n}']
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        dp[key] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        return dp[key]


if __name__ == '__main__':
    print(Solution().uniquePaths(2, 3))
