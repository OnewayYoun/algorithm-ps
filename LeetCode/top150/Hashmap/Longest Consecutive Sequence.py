import heapq
from collections import defaultdict
from typing import List


class Solution:
    """
    Input: nums = [100,4,200,1,3,2]
    Output: 4

    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9
    """

    # O(nlog(n))
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dd = defaultdict(int)
        nums.sort()

        for num in nums:
            dd[num] = 1 + dd[num - 1] + dd[num + 1]

        return max(dd.values())

    # O(nlog(n))
    def longestConsecutive2(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        answer = 1
        nums = list(set(nums))
        nums.sort()
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 1

        return answer

    # O(n)
    def longestConsecutive3(self, nums: List[int]) -> int:
        nums_set = set(nums)
        answer = 0
        visited = set()
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            cnt = 0
            while (num + cnt) in nums_set:
                cnt += 1
                visited.add(num)
            answer = max(answer, cnt)
        return answer

    def longestConsecutive4(self, nums: List[int]) -> int:
        pass


print(Solution().longestConsecutive3([100, 4, 200, 1, 3, 2]))
