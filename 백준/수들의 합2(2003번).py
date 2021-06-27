'''
4 2
1 1 1 1
answer = 3
10 5
1 2 3 4 2 5 3 1 1 2
answer = 3
'''

n, m = map(int, input().split())
pers = list(map(int, input().split()))
end = 0
sum = 0
answer = 0


for start in range(n):
    while sum < m and end < n:
        sum += pers[end]
        end += 1
    if sum == m:
        answer += 1
    sum -= pers[start]

print(answer)


#출처: 백준 온라인 저지, https://www.acmicpc.net/problem/2003