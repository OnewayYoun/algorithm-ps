class Solution:
    """
    Input: n = 11
    Output: 3

    Input: n = 128
    Output: 1

    Input: n = 2147483645
    Output: 30
    """

    def hammingWeight(self, n: int) -> int:
        return format(n, 'b').count('1')

    def hammingWeight1(self, n: int) -> int:
        answer = 0
        while n:
            answer += n % 2
            n >>= 1  # same as n //= 2
        return answer

    def hammingWeight2(self, n: int) -> int:
        answer = 0
        while n:
            n = n & (n - 1)
            answer += 1
        return answer


print(Solution().hammingWeight(11))
print(Solution().hammingWeight1(11))
print(Solution().hammingWeight2(11))
