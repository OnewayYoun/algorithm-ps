from sys import stdin
from collections import deque

input = stdin.readline

n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
  x, y = map(int, input().split())
  graph[x][y] = 1
  graph[y][x] = 1

def DFS(v):
  visited[v] = True
  print(v, end=' ')

  for i in range(n+1):
    if not visited[i] and graph[v][i] == 1:
      DFS(i)

def BFS(v):
  visited[v] = False
  q = deque([v])

  while q:
    v = q.popleft()
    print(v, end = ' ')

    for i in range(n+1):
      if visited[i] and graph[v][i] == 1:
        q.append(i)
        visited[i] = False

DFS(v)
print()
BFS(v)

'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''