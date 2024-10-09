n = int(input())
input_moves = input().split()

x, y = 1, 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
moves = ['R', 'L', 'D', 'U']

for move in input_moves:
    for i in range(len(moves)):
        if move == moves[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if 1 <= nx <= n and 1 <= ny <= n:
        x = nx
        y = ny

print(ny, nx)
