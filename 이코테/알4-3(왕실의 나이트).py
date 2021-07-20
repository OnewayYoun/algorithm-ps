curr = input()
curr_row = int(curr[1])
curr_col = ord(curr[0])-96

cnt = 0

types = [
  (1, 2), (-1, 2), (1, -2), (-1, -2),
  (2, 1), (-2, 1), (2, -1), (-2, -1)
  ]

for i in range(len(types)):
  if 1 <= (types[i][0] + curr_row) <= 8 and 1 <= (types[i][1] + curr_col) <= 8:
    cnt += 1

print(cnt)