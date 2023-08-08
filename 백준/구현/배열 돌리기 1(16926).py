import sys


def get_chain(start, n, m, graph):
    chain = [0] * (2 * (n + m - 2))
    i, j, idx = start, start, 0
    for _ in range(n - 1):
        chain[idx] = graph[i][j]
        i += 1
        idx += 1
    for _ in range(m - 1):
        chain[idx] = graph[i][j]
        j += 1
        idx += 1
    for _ in range(n - 1):
        chain[idx] = graph[i][j]
        i -= 1
        idx += 1
    for _ in range(m - 1):
        chain[idx] = graph[i][j]
        j -= 1
        idx += 1
    return chain


def set_chain(start, n, m, graph, new_graph):
    i, j, idx = start, start, 0
    for _ in range(n - 1):
        graph[i][j] = new_graph[idx]
        i += 1
        idx += 1
    for _ in range(m - 1):
        graph[i][j] = new_graph[idx]
        j += 1
        idx += 1
    for _ in range(n - 1):
        graph[i][j] = new_graph[idx]
        i -= 1
        idx += 1
    for _ in range(m - 1):
        graph[i][j] = new_graph[idx]
        j -= 1
        idx += 1


def rotate(start, N, M, R, graph):
    chain = get_chain(start, N - 2 * start, M - 2 * start, graph)
    length = len(chain)
    new_chain = chain[-R % length:] + chain[:-R % length]
    set_chain(start, N - 2 * start, M - 2 * start, graph, new_chain)


if __name__ == '__main__':
    N, M, R = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    for start in range(min(N, M) // 2):
        rotate(start, N, M, R, graph)

    for i in graph:
        print(*i, sep=' ')
