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


print(Solution().climbStairs(4))
