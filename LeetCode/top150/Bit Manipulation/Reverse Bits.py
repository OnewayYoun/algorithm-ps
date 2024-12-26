class Solution:
    """
    Input: n = 00000010100101000001111010011100
    Output:    964176192 (00111001011110000010100101000000)
    Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
    so return 964176192 which its binary representation is 00111001011110000010100101000000.

    Input: n = 11111111111111111111111111111101
    Output:   3221225471 (10111111111111111111111111111111)
    Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293,
    so return 3221225471 which its binary representation is 10111111111111111111111111111111.
    """

    def reverseBits(self, n: int) -> int:
        n = str(format(n, 'b'))
        while len(n) != 32:
            n = '0' + n
        return int(n[::-1], 2)

    def reverseBits1(self, n: int) -> int:
        n = str(format(n, 'b')).zfill(32)
        return int(n[::-1], 2)


print(Solution().reverseBits(43261596))
