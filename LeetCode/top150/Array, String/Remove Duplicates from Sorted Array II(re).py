from typing import List


class Solution:
    """
    Input: nums = [1,1,1,2,2,3]
    Output: 5, nums = [1,1,2,2,3,_]

    Input: nums = [0,0,1,1,1,1,2,3,3]
    Output: 7, nums = [0,0,1,1,2,3,3,_,_]
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i < 2 or nums[i - 2] != num:
                nums[i] = num
                i += 1
        return i

    def removeDuplicates1(self, nums: List[int]) -> int:
        idx = 0
        cnt = float('inf')
        cur_num = float('-inf')
        for num in nums:
            if num != cur_num:
                cur_num = num
                cnt = 0
            if cnt < 2:
                nums[idx] = cur_num
                idx += 1
            cnt += 1
        return idx

# print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
print(Solution().removeDuplicates1([0, 0, 1, 1, 1, 1, 2, 3, 3]))
