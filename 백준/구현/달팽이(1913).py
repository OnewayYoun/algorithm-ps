import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N, target_num = int(input()), int(input())
    graph = [[None] * N for _ in range(N)]
    direction = 0  # 0: 하, 1: 우, 2: 상, 3: 좌
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    curr_val = N * N
    curr_x, curr_y = 0, 0
    target_loc = []

    while curr_val > 0:
        if curr_val == target_num:
            target_loc = [curr_y + 1, curr_x + 1]
        graph[curr_y][curr_x] = curr_val
        new_x, new_y = curr_x + dx[direction], curr_y + dy[direction]

        if 0 <= new_x < N and 0 <= new_y < N and graph[new_y][new_x] is None:
            curr_x, curr_y = new_x, new_y
        else:
            direction = (direction + 1) % 4
            curr_x, curr_y = curr_x + dx[direction], curr_y + dy[direction]
        curr_val -= 1

    for i in graph:
        print(*i, sep=' ')
    print(*target_loc, sep=' ')
