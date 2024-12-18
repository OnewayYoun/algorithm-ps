from typing import List
from collections import Counter


class Solution:
    """
    Input: nums = [1,1,1,2,2,3]
    Output: 5, nums = [1,1,2,2,3,_]

    Input: nums = [0,0,1,1,1,1,2,3,3]
    Output: 7, nums = [0,0,1,1,2,3,3,_,_]
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        idx = 0
        for key, val in sorted(cnt.items()):
            for _ in range(2):
                nums[idx] = key
                idx += 1
                if val == 1:
                    break

        return idx


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        cur_num = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if cur_num == nums[i] and cnt < 2:
                nums[idx] = cur_num
                idx += 1
                cnt += 1
            elif cur_num != nums[i]:
                cnt = 1
                cur_num = nums[i]
                nums[idx] = cur_num
                idx += 1
        return idx


print(Solution2().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
