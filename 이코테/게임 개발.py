'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''

n, m = map(int, input().split())
x, y, d = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
maps = [input().split() for _ in range(n)]
maps[x][y] = '2'
cnt = 1

while True:
    flag = False
    for _ in range(4):
        d = (d + 3) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if maps[nx][ny] == '1':
            continue
        if maps[nx][ny] == '0':
            flag = True
            cnt += 1
            maps[nx][ny] = '2'
            x, y = nx, ny
            break
    if not flag:
        if maps[x + dx[d - 2]][y + dy[d - 2]] == '1':
            break
        else:
            x, y = x + dx[d - 2], y + dy[d - 2]

print(cnt)
