from collections import deque


def bfs(X, Y, maps):
    dq = deque([(0, 0)])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not 0 <= nx < X or not 0 <= ny < Y:
                continue
            if maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                dq.append((nx, ny))


def solution(maps):
    X, Y = len(maps[0]), len(maps)
    bfs(X, Y, maps)
    if maps[Y - 1][X - 1] <= 1:
        return -1
    return maps[Y - 1][X - 1]


if __name__ == '__main__':
    maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]  # 11
    # maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]    # -1
    print(solution(maps))
