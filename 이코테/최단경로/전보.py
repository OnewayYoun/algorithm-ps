import heapq
import sys

input = sys.stdin.readline

n, m, start = map(int, input().split())
distance = [float("inf")] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


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

cnt = 0
max_distance = 0
for idx, val in enumerate(distance):
    if idx == start or val == float("inf"):
        continue
    cnt += 1
    max_distance = max(max_distance, val)

print(cnt, max_distance)

"""
3 2 1
1 2 4
1 3 2
"""
