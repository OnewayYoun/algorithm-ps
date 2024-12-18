class Solution:
    """
    Input: n = 19
    Output: true

    Input: n = 2
    Output: false
    """

    def isHappy(self, n: int) -> bool:
        num_set = set()

        total = 0
        while True:
            for i in str(n):
                total += int(i) ** 2
            n = total
            if n == 1:
                return True
            if n in num_set:
                return False
            num_set.add(n)
            total = 0


print(Solution().isHappy(19))
