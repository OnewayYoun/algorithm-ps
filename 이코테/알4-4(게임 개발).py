n, m = map(int, input().split())
x, y, d = map(int, input().split())

map_initial = [[0]*m for _ in range(n)]
map_input = [ list(map(int, input().split())) for _ in range(n) ]

map_initial[x][y] = 1
cnt = 1

# [북, 동, 남, 서]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3

turn_times = 0

while True:
  turn_left()
  next_x = x + dx[d]
  next_y = y + dy[d]

  if map_initial[next_x][next_y] == 0 and map_input[next_x][next_y] == 0:
    map_initial[next_x][next_y] = 1
    cnt += 1
    x = next_x
    y = next_y

    turn_times = 0
    continue

  else:
    turn_times += 1

  if turn_times == 4:
    next_x = x - dx[d]
    next_y = y - dy[d]
    
    if map_input[next_x][next_y] == 0:
      x = next_x
      y = next_y
      turn_times = 0
    else:
      break


print(cnt)
