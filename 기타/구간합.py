n = 5
data = [10, 20, 30, 40, 50]

sum = 0
prefix_sum = [0]

for i in data:
    sum += i
    prefix_sum.append(sum)

# 2~4까지 구하기
L, R = 2, 4

print(prefix_sum)
print()
print(prefix_sum[R] - prefix_sum[L-1])

