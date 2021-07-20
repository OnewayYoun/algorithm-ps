n = int(input())
walks = input().split()

x = 1
y = 1

types = ['L', 'R', 'U', 'D']
xx = [0, 0, -1, 1]
yy = [-1, 1, 0, 0]

for i in walks:
  for j in range(4):
    if i == types[j]:
      temp_x = x + xx[j]
      temp_y = y + yy[j]
  if temp_x<1 or temp_y<1 or temp_x>n or temp_y>n:
    continue
  else:
    x = temp_x
    y = temp_y

print(x, y)