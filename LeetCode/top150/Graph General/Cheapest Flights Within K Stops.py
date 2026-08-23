from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmp = prices[:]
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tmp[d]:
                    tmp[d] = prices[s] + p
            prices = tmp

        return prices[dst] if prices[dst] != float('inf') else -1


print(Solution().findCheapestPrice(n=5, flights=[[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], src=2,
                             dst=1, k=1))
