from collections import deque

n = int(input())
time = [0] * (n + 1)
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for curse_num in data[1:-1]:
        indegree[i] += 1
        graph[curse_num].append(i)

answer = time[:]


def topology_sort():
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            answer[i] = max(time[i] + answer[now], answer[i])
            if indegree[i] == 0:
                q.append(i)


topology_sort()
print(answer)

"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""
