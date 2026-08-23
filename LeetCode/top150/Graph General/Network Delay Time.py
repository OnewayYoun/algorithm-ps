import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for s, d, w in times:
            edges[s].append((d, w))

        hq = [(0, k)]
        visited = set()
        answer = 0

        while hq:
            weight, node = heapq.heappop(hq)
            if node in visited:
                continue

            visited.add(node)
            answer = max(answer, weight)

            for d, w in edges[node]:
                if d not in visited:
                    heapq.heappush(hq, (weight + w, d))

        return answer if len(visited) == n else -1

print(Solution().networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1], [2, 5, 10]], n=5, k=2))
