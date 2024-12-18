from typing import List


class Solution:
    """
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]

    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        print(nums)
        return len(nums)


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        cur_num = nums[0]
        for i in range(1, len(nums)):
            if cur_num != nums[i]:
                nums[idx] = nums[i]
                cur_num = nums[i]
                idx += 1
        return idx


print(Solution2().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
