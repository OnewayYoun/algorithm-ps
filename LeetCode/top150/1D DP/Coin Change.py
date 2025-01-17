from typing import List


class Solution:
    """
    Input: coins = [1,2,5], amount = 11
    Output: 3

    Input: coins = [2], amount = 3
    Output: -1

    Input: coins = [1], amount = 0
    Output: 0
    """

    # Bottom-Up
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    # Top-Down
    def coinChange1(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(rem):
            if rem < 0:
                return float('inf')
            if rem == 0:
                return 0
            if rem in memo:
                return memo[rem]

            min_coins = float('inf')
            for coin in coins:
                min_coins = min(min_coins, dfs(rem - coin) + 1)

            memo[rem] = min_coins
            return min_coins

        result = dfs(amount)
        return result if result != float('inf') else -1


print(Solution().coinChange1(coins=[1, 2, 5], amount=11))
