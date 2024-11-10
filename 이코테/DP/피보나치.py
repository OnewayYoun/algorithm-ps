def fibo_recursive(x):
    if x == 1 or x == 2:
        return 1
    return fibo_recursive(x - 2) + fibo_recursive(x - 1)


dp = [0] * 100


def fibo(x):
    if x == 1 or x == 2:
        return 1
    if dp[x] != 0:
        return dp[x]
    dp[x] = fibo(x - 2) + fibo(x - 1)
    return dp[x]


print(fibo(5))
