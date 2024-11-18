"""
4
1 3 1 5
"""

n = int(input())
l = list(map(int, input().split()))

dp = [0] * n
dp[0] = l[0]
dp[1] = max(l[0], l[1])

for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + l[i])

print(dp[n - 1])

dp = {}


def recursive(i):
    if i == 0:
        return l[0]
    if i == 1:
        return max(l[0], l[1])
    dp[i] = max(recursive(i - 1), recursive(i - 2) + l[i])
    return dp[i]


print(recursive(len(l) - 1))
