import math


class Solution:
    """
    Input: x = 4
    Output: 2

    Input: x = 8
    Output: 2
    """

    def mySqrt(self, x: int) -> int:
        return math.trunc(x ** (1 / 2))

    def mySqrt1(self, x: int) -> int:
        left, right = 0, x
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 < x:
                result = mid
                left = mid + 1
            elif mid ** 2 > x:
                right = mid - 1
            else:
                return mid
        return result


print(Solution().mySqrt1(8))
