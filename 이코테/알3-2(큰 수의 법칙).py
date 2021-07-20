n, m, k = map(int, input().split())
a = list(map(int, input().split()))
result = 0
a.sort(reverse = True)

big_1st = a[0]
big_2nd = a[1]

while True:
  for i in range(k):
    if m == 0:
      break
    result += big_1st
    m -= 1

  if m == 0:
    break

  result += big_2nd
  m -= 1

print(result)