from functools import reduce
from typing import List
import heapq


class Solution:
    """
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5

    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for i in range(k - 1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)













    def findKthLargest1(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        answer = None
        for _ in range(k):
            answer = heapq.heappop(nums)
        return -answer


print(Solution().findKthLargest2(nums=[3, 2, 1, 5, 6, 4], k=2))
