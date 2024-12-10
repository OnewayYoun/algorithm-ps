from typing import List


class Solution:
    """
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        cnt_zero = 0
        answer = []
        for num in nums:
            if num == 0:
                cnt_zero += 1
            else:
                total *= num

        for num in nums:
            if cnt_zero == 0:
                answer.append(total // num)
            elif cnt_zero == 1:
                if num == 0:
                    answer.append(total)
                else:
                    answer.append(0)
            else:
                answer.append(0)
        return answer

    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer


# print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
print(Solution().productExceptSelf1([1, 2, 3, 4]))
# print(Solution().productExceptSelf1([-1, 1, 0, -3, 3]))
