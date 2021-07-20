n = int(input())
a = []

def setting(data):
  return data[1]

for i in range(n):
  temp = input().split()

  a.append( (temp[0], int(temp[1])) )

a.sort(key = lambda a: a[1])

for i in a:
  print(i[0], end=' ')

print(a)
print(setting(a))