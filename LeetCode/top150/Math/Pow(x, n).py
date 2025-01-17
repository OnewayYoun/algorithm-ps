class Solution:
    """
    Input: x = 2.00000, n = 10
    Output: 1024.00000

    Input: x = 2.10000, n = 3
    Output: 9.26100

    Input: x = 2.00000, n = -2
    Output: 0.25000
    """

    # 2 * 2 * 2 * 2 * 2

    def myPow(self, x: float, n: int) -> float:
        return x ** n

    def myPow1(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        half = self.myPow1(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x


print(Solution().myPow1(x=2.00000, n=10))
