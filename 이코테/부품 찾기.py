n = 5
l = [8, 3, 7, 9, 2]
m = 3
target = [5, 7, 9]


def binary_search(l, start, end, target):
    if start > end:
        return
    mid = (start + end) // 2
    if l[mid] == target:
        return mid
    elif l[mid] > target:
        return binary_search(l, start, mid - 1, target)
    else:
        return binary_search(l, mid + 1, end, target)


l.sort()

for i in target:
    if binary_search(l, 0, n - 1, i) is None:
        print('no', end=' ')
    else:
        print('yes', end=' ')