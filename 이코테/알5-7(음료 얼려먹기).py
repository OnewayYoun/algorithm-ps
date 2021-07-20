n, m = map(int, input().split())

g_in = []

for i in range(n):
  g_in.append(list(map(int, input())))

def dfs(x, y):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  
  if g_in[x][y] == 0:
    g_in[x][y] = 1

    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True

  return False

cnt = 0

for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      cnt += 1

print(cnt)

for i in g_in:
  print(*i)