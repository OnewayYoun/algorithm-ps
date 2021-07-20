n = int(input())

an = list(map(int, input().split()))
an.sort()

m = int(input())

am = list(map(int, input().split()))


def bin_search(array, target, start, end):
    if start > end:
        return 'no'

    mid = (start + end) // 2

    if array[mid] == target:
        return 'yes'

    elif array[mid] > target:
        return bin_search(array, target, start, mid - 1)

    else:
        return bin_search(array, target, mid + 1, end)


for i in am:
    print(bin_search(an, i, 0, n - 1), end=' ')
