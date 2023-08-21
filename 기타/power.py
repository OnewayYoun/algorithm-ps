def power(x: int, n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return x
    tmp = power(x, n // 2)
    if n % 2 == 0:
        return tmp * tmp
    else:
        return tmp * tmp * x


print(power(2, 10))


def power(x, n):
    result = 1
    while n > 0:
        if n & 1:  # If n is odd, multiply result by x
            result *= x
        x *= x
        n >>= 1  # Right shift n by 1 (equivalent to dividing n by 2)
    return result


print(power(2, 13))
