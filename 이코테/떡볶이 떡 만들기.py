"""
4 6
19 15 10 17
"""

n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
result = 0


def binary_search_iterative(l, start, end):
    global result
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for i in l:
            if i > mid:
                total += i - mid
        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1


binary_search_iterative(l, 0, max(l))
print(result)
