n = int(input())
l = {key: val for _ in range(n) for key, val in [input().split()]}

for i in sorted(l.items(), key=lambda x: x[0]):
    print(i[0], end=' ')
