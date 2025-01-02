from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    """
    Input: citations = [3,0,6,1,5]
    Output: 3
    Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
    Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

    Input: citations = [1,3,1]
    Output: 1
    """

    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        right = len(citations) - 1
        answer = 0

        for i in range(citations[-1] + 1):
            if i <= right - bisect_left(citations, i) + 1:
                answer = i
            else:
                break
        return answer

    def hIndex1(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0

        for i, c in enumerate(citations):
            if i < c:
                h_index = i + 1
            else:
                break

        return h_index


print(Solution().hIndex1([5, 5, 5, 5]))
