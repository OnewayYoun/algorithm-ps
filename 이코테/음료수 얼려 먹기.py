'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

4 5
00110
00011
11111
00000
'''

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if graph[x][y] == '0':
        graph[x][y] = '1'
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
    return


n, m = map(int, input().split())
graph = [[char for char in input()] for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '0':
            cnt += 1
            dfs(i, j)

print(cnt)
