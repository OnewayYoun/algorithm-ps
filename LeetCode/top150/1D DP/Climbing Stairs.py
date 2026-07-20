from collections import defaultdict


class Solution:
    """
    Input: n = 2
    Output: 2

    Input: n = 3
    Output: 3
    """

    def climbStairs(self, n: int) -> int:
        dp = defaultdict()
        dp[0], dp[1], dp[2] = 0, 1, 2

        def fibo(number):
            if number in dp:
                return dp[number]
            dp[number] = fibo(number - 1) + fibo(number - 2)
            return dp[number]

        return fibo(n)

    def climbStairs_bottom_up(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]

    def climbStairs_top_down(self, n: int) -> int:
        memo = {}

        def dfs(k):
            if k <= 2:
                return k
            if k in memo:
                return memo[k]

            memo[k] = dfs(k - 1) + dfs(k - 2)
            return memo[k]

        return dfs(n)


print(Solution().climbStairs_top_down(4))