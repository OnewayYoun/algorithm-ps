dp = [[0] * 100 for _ in range(100)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            dp[k][j] = 1

answer = 0
for i in dp:
    answer += sum(i)
print(answer)
