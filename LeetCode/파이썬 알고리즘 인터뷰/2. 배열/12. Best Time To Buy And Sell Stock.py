from typing import List


class Solution:
    """
    Input: prices = [7,1,5,3,6,4]
    Output: 5

    Input: prices = [7,6,4,3,1]
    Output: 0
    """

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_val = float('inf')

        for price in prices:
            min_val = min(min_val, price)
            max_profit = max(max_profit, price - min_val)

        return max_profit

    """
    Best Time to Buy and Sell Stock II
    
    Input: prices = [7,1,5,3,6,4]
    Output: 7
    
    Input: prices = [1,2,3,4,5]
    Output: 4
    
    Input: prices = [7,6,4,3,1]
    Output: 0
    """

    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            if i == 0:
                continue
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i - 1]
        return profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
