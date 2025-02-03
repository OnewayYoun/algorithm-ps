from typing import List
from collections import defaultdict, deque


class Solution:
    """
    Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

    Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    Output: [3.75000,0.40000,5.00000,0.20000]

    Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
    Output: [0.50000,2.00000,-1.00000,-1.00000]
    """

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for idx, eq in enumerate(equations):
            a, b = eq
            graph[a].append([b, values[idx]])
            graph[b].append([a, 1 / values[idx]])

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0

            dq = deque()
            dq.append([start, 1])
            visited = set()
            visited.add(start)
            while dq:
                node, weight = dq.popleft()
                if node == end:
                    return weight
                for path in graph[node]:
                    if path[0] not in visited:
                        dq.append([path[0], weight * path[1]])
                        visited.add(path[0])

            return -1.0

        return [bfs(query[0], query[1]) for query in queries]


print(Solution().calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                              queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
