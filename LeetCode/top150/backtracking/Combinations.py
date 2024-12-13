from typing import List
from itertools import combinations


class Solution:
    """
    Input: n = 4, k = 2
    Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

    Input: n = 1, k = 1
    Output: [[1]]
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(map(list, combinations(range(1, n + 1), k)))

    def combine1(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def dfs(start, cur):
            if len(cur) == k:
                answer.append(cur[:])
                return
            for i in range(start, n + 1):
                cur.append(i)
                dfs(i + 1, cur)
                cur.pop()

        dfs(1, [])

        return answer

    def combine2(self, n: int, k: int) -> List[List[int]]:
        answer = []
        numbers = [*range(1, n + 1)]

        def dfs(idx, cur):
            if len(cur) == k:
                answer.append(cur[:])
                return

            for i in range(idx, n):
                cur.append(numbers[i])
                dfs(i + 1, cur)
                cur.pop()

        dfs(0, [])

        return answer


# print(Solution().combine(n=4, k=2))
# print(Solution().combine1(n=4, k=2))
print(Solution().combine2(n=4, k=2))
