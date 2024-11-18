n = int(input())
l = list(map(int, input().split()))

dp = [0] * n
dp[0] = l[0]
dp[1] = max(l[0], l[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + l[i])

print(dp[n-1])