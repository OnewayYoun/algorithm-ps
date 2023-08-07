import sys
from collections import deque, defaultdict


def topology_sort():
    q = deque()
    result = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(' '.join(map(str, result)))


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    indegree = defaultdict(int)
    graph = defaultdict(list)

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1

    topology_sort()
