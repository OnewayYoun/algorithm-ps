import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드 갯수, 간선 갯수, 시작노드
n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_distance = 0

for i in distance:
  if i != INF:
    count += 1
    max_distance = max(max_distance, i)

print(distance)
print(graph)
print(count-1, max_distance)

'''
3 2 1
1 2 4
1 3 2
'''