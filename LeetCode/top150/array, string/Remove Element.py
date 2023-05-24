from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        answer = len(nums)
        for i, v in enumerate(nums):
            if v == val:
                answer -= 1
                nums[i] = '_'
        nums.sort(key=lambda x: str(x))
        return answer


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2

    # k = 5
    # nums = [0, 1, 4, 0, 3, '_', '_', '_']

    print(Solution().removeElement(nums, val))
