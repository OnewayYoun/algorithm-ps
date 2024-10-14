def quick_sort(l, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and l[left] <= l[pivot]:
            left += 1
        while right > start and l[right] >= l[pivot]:
            right -= 1
        if left > right:
            l[right], l[pivot] = l[pivot], l[right]
        else:
            l[left], l[right] = l[right], l[left]
    quick_sort(l, start, right - 1)
    quick_sort(l, right + 1, end)


tmp = [5, 1, 3, 6, 32, 7, 9]
quick_sort(tmp, 0, len(tmp) - 1)
print(tmp)
