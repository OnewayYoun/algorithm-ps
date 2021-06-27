'''
10 15
5 1 3 5 10 7 4 9 2 8
answer = 2
'''

n, s = map(int, input().split())
pers = list(map(int, input().split()))
end = 0
sum = 0
length = int(1e10)

for start in range(n):
    while sum < s and end < n:
        sum += pers[end]
        end += 1
    if sum >= s:
        length = min(length, (end-start))
    if sum < s and start == 0:
        length = 0
    sum -= pers[start]

print(length)

#출처: 백준 온라인 저지, https://www.acmicpc.net/problem/1806
