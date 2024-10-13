from collections import deque
from pprint import pprint

'''
5 6
101010
111111
000001
111111
111111
'''


def bfs(start: tuple):
    q = deque([start])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] += graph[x][y]


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
graph = [[int(char) for char in input()] for _ in range(n)]

bfs((0, 0))
pprint(graph)
print(graph[n - 1][m - 1])
