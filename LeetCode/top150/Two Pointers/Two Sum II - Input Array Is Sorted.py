from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            added = numbers[left] + numbers[right]
            if added == target:
                return [left+1, right+1]
            if added > target:
                right -= 1
            else:
                left += 1


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 22
    answer = [2, 4]

    print(Solution().twoSum(numbers, target))