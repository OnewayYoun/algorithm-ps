from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_val = prices[0]

        for price in prices:
            if price < min_val:
                min_val = price
            elif price > min_val:
                max_profit = max(max_profit, price - min_val)

        return max_profit


print(Solution().maxProfit([7, 3, 5, 1, 6, 4]))
