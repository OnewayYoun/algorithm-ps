n, k = map(int, input().split())

a = []
for i in range(2):
  a.append(list(map(int, input().split())))
  a[i].sort()

for i in range(k):
  if a[0][i] < a[1][-1-i]:
    a[0][i], a[1][-1-i] = a[1][-1-i], a[0][i]

print(sum(a[0]))