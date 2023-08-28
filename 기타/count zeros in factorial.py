# def count_zeros(N):
#     two_cnts = 0
#     five_cnts = 0
#     for i in range(1, N + 1):
#         while i % 2 == 0:
#             i //= 2
#             two_cnts += 1
#         while i % 5 == 0:
#             i //= 5
#             five_cnts += 1
#     return min(two_cnts, five_cnts)
#
#
# print(count_zeros(100))


from collections import defaultdict


def count_zeros(n, dp=defaultdict(int)):
    if n in dp:
        return dp[n]
    dp[n] = count_zeros(n // 5) + 1 if not n % 5 else 0
    return dp[n]


answer = 0
for i in range(1, 101):
    answer += count_zeros(i)
print(answer)
