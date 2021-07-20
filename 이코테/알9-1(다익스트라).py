import sys
input = sys.stdin.readline
INF = int(1e9) #무한을 의미하는 값으로 10억 설정

#노드 갯수, 간선 갯수 입력받기
n, m = map(int, input().split())
#시작노드
start = int(input())

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(n+1)]
#방문테이블 false로 초기화
visited = [False] * (n+1)
#최단거리 테이블 모두 무한대로 초기화
distance = [INF] * (n+1)

for _ in range(m):
  #a번 노드에서 b번 노드로 가는 비용이 c
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]

  for i in range(n-1):
    now = get_smallest_node()
    visited[now] = True

    for j in graph[now]:
      cost = distance[now] + j[1]
      if cost < distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])

'''
input:
6 11
1
1 2 2
1 3 5
1 4 1 
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''