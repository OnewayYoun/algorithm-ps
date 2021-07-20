n, m = map(int, input().split())
cards = []
result = []

for i in range(n):
  cards.append(list(map(int, input().split())))
  result.append(min(cards[i]))

print(max(result))


#for i in cards:
#  print(*i)

'''
n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  result = max(result, min_value)

print(result)
'''