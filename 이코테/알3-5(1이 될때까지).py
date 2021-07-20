num, divider = map(int, input().split())
cnt = 0

while num != 1:
  if num%divider == 0:
    num //= divider
    cnt += 1
  else:
    num -= 1
    cnt += 1

print(cnt)