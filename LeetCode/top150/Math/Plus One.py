from typing import List


class Solution:
    """
    Input: digits = [1,2,3]
    Output: [1,2,4]

    Input: digits = [4,3,2,1]
    Output: [4,3,2,2]

    Input: digits = [9]
    Output: [1,0]
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join(map(str, digits))) + 1
        return [int(i) for i in str(number)]

    def plusOne1(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        idx, flag = 0, True

        while flag:
            if idx >= len(digits):
                digits.append(1)
                break
            if digits[idx] < 9:
                digits[idx] += 1
                flag = False
            else:
                digits[idx] = 0
                idx += 1
        return digits[::-1]


# print(Solution().plusOne([4, 3, 2, 1]))
print(Solution().plusOne1([9, 9]))
