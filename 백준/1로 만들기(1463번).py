num = int(input())

dp = [0] * (num+1)

for i in range(2, num+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[num])


#출처: 백준 온라인 저지, https://www.acmicpc.net/problem/1463