n, m = map(int, input().split())
choices = [int(input()) for _ in range(n)]
dp = [0] + [float("inf")] * m

for choice in choices:
    for i in range(choice, m + 1):
        dp[i] = min(dp[i], dp[i - choice] + 1)

if dp[m] != float("inf"):
    print(dp[m])
else:
    print(-1)
