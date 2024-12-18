from typing import List


class Solution:
    """
    Input: nums = [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]

    Input: nums = [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    """

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        lst = []
        tmp = str(nums[0])
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                tmp += ',' + str(nums[i])
            else:
                lst.append(tmp)
                tmp = str(nums[i])
        lst.append(tmp)

        answer = []
        for i in lst:
            tmp = i.split(',')
            if len(tmp) == 1:
                answer.append(tmp[0])
            else:
                answer.append(f'{tmp[0]}->{tmp[-1]}')
        return answer

    def summaryRanges1(self, nums: List[int]) -> List[str]:
        answer = []

        i = 0
        while i < len(nums):
            start = nums[i]
            while i < len(nums) - 1 and nums[i + 1] - nums[i] == 1:
                i += 1
            if start == nums[i]:
                answer.append(str(start))
            else:
                answer.append(f'{start}->{nums[i]}')
            i += 1
        return answer

    def summaryRanges2(self, nums: List[int]) -> List[str]:
        tmp = []
        for num in nums:
            if tmp and tmp[-1][1] == num - 1:
                tmp[-1][1] = num
            else:
                tmp.append([num, num])

        return [f'{x}' if x == y else f'{x}->{y}' for x, y in tmp]


# print(Solution().summaryRanges1([0, 1, 2, 4, 5, 7]))
print(Solution().summaryRanges2([0, 1, 2, 4, 5, 7]))
