from typing import List
from collections import Counter, defaultdict


class Solution:
    """
    Input: nums = [3,2,3]
    Output: 3

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
    """

    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        dd = defaultdict(int)
        for i in nums:
            dd[i] += 1
        return sorted(dd.items(), key=lambda x: x[1], reverse=True)[0][0]


class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
