def binary_search_recursive(l, target, start, end):
    if start > end:
        return
    mid = (start + end) // 2

    if l[mid] == target:
        return mid
    elif l[mid] > target:
        return binary_search_recursive(l, target, start, mid - 1)
    else:
        return binary_search_recursive(l, target, mid + 1, end)


def binary_search_iterative(l, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if l[mid] == target:
            return mid
        elif l[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


l = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
result = binary_search_recursive(l, 5, 0, len(l) - 1)
if result is None:
    print('target number does not exist')
else:
    print(result)

result = binary_search_iterative(l, 6, 0, len(l) - 1)
if result is None:
    print('target number does not exist')
else:
    print(result)
