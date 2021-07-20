# 플로이드 워셜(미래도시)
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

for _ in range(m):
  a, b = map(int, input().split())
  # 간선정보를 입력받고 양방향 비용 1로 설정
  graph[a][b], graph[b][a] = 1, 1

# 거쳐 갈 노드k, 최종 목적지 노드 x 입력받기
x, k = map(int, input().split())

for i in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

result = graph[1][k] + graph[k][x]

# result = INF + INF or INF + 1 or 기타등등이 발생할수있기에 >= INF사용
if result >= INF:
  print('-1')
else:
  print(result)







'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''