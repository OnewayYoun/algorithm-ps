from collections import defaultdict
from typing import List


class Solution:
    """
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]

    Input: numbers = [2,3,4], target = 6
    Output: [1,3]

    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]

    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        dd = defaultdict(int)

        for idx, num in enumerate(numbers):
            if target - num in dd:
                return [dd[target - num], idx + 1]
            else:
                dd[num] = idx + 1

        return []


print(Solution().twoSum1(numbers=[2, 7, 11, 15], target=9))
