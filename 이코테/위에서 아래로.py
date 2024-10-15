n = int(input())
l = [int(input()) for _ in range(n)]

l.sort(reverse=True)
print(*l)