from functools import reduce
from typing import List


class Solution:
    """
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt_zero = 0
        total = reduce(lambda x, y: x * y, filter(lambda x: x != 0, nums), 1)
        for num in nums:
            if num == 0:
                cnt_zero += 1
        if cnt_zero > 1:
            return [0 for _ in range(len(nums))]
        elif cnt_zero == 1:
            return [total if num == 0 else 0 for num in nums]
        return [total // num for num in nums]

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        left_sum, right_sum = 1, 1
        product_sum_right = [1]
        product_sum_left = [1]

        for i in range(len(nums)):
            right_sum *= nums[i]
            left_sum *= nums[-i - 1]
            product_sum_right.append(right_sum)
            product_sum_left.append(left_sum)
        product_sum_left = product_sum_left[::-1]

        return [product_sum_right[i] * product_sum_left[i + 1] for i in range(len(nums))]


# print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
print(Solution().productExceptSelf2([2, 2, 3, 4]))
