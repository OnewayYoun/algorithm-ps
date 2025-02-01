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

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange1(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(rem):
            if rem < 0:
                return float('inf')
            if rem == 0:
                return 0
            if rem in cache:
                return cache[rem]

            min_coin = float('inf')
            for coin in coins:
                min_coin = min(min_coin, dfs(rem - coin) + 1)

            cache[rem] = min_coin
            return min_coin

        result = dfs(amount)
        return result if result != float('inf') else -1


# print(Solution().coinChange(coins=[1, 2, 5], amount=11))
print(Solution().coinChange1(coins=[1, 2, 5], amount=11))
