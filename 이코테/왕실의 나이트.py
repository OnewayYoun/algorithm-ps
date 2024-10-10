loc = input()
x, y = int(loc[1]), ord(loc[0]) - ord('a') + 1

print(y)

moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, 1), (2, -1), (1, -2), (1, 2)]

cnt = 0
for move in moves:
    if 1 <= x + move[0] <= 8 and 1 <= y + move[1] <= 8:
        cnt += 1

print(cnt)
