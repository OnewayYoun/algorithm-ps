from typing import List
from itertools import product
import heapq


class Solution:
    """
    Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
    Output: [[1,2],[1,4],[1,6]]

    Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
    Output: [[1,1],[1,1]]
    """

    # memory limit exceeded
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        hq = []
        for prod in product(nums1[:k], nums2[:k]):
            heapq.heappush(hq, [sum(prod)] + list(prod))
        return [[x[1], x[2]] for x in (heapq.heappop(hq) for _ in range(k))]

    def kSmallestPairs1(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pass


print(Solution().kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))
# print(Solution().kSmallestPairs1(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))
