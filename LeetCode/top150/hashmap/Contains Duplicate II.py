from collections import deque
from typing import List


class Solution:
    """
    Input: nums = [1,2,3,1], k = 3
    Output: true

    Input: nums = [1,0,1,1], k = 1
    Output: true

    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dq = deque()
        check = set()
        cnt = 0

        for num in nums:
            if num in check:
                return True
            dq.append(num)
            check.add(num)
            if cnt < k:
                cnt += 1
            else:
                check.remove(dq.popleft())
        return False

    # sliding window
    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        left = 0
        visited = set()
        for right in range(len(nums)):
            if nums[right] in visited:
                return True
            if right - left >= k:
                visited.remove(nums[left])
                left += 1
            visited.add(nums[right])
        return False


print(Solution().containsNearbyDuplicate1(nums=[1, 2, 1], k=0))
# print(Solution().containsNearbyDuplicate1(nums=[1, 2, 3, 1], k=3))
