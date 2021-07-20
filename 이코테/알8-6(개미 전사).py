n = int(input())
a = list(map(int, input().split()))
d = [0] * 100

d[0] = a[0]
d[1] = max(a[0], a[1])

for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + a[i])

print(d[n-1])