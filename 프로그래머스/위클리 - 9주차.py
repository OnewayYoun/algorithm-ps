from collections import defaultdict, deque
from itertools import combinations


def bfs(visited, d):
    cnt = 1
    visited[1] = True
    dq = deque([1])

    while dq:
        v = dq.popleft()
        for i in d[v]:
            if not visited[i]:
                cnt += 1
                visited[i] = True
                dq.append(i)

    return cnt


def solution(n, wires):
    answer = []

    for com in combinations(wires, len(wires)-1):
        d = defaultdict(list)
        for i in com:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        visited = [False] * (n+1)
        tmp = bfs(visited, d)
        answer.append(abs(n-tmp-tmp))

    return min(answer)


if __name__ == '__main__':
    n, wires, result = 9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]], 3
    print(solution(n, wires))

    n, wires, result = 4, [[1, 2], [2, 3], [3, 4]], 0
    print(solution(n, wires))

    n, wires, result = 7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]], 1
    print(solution(n, wires))
