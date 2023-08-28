def quick_sort(lst, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and lst[pivot] >= lst[left]:
            left += 1
        while right > start and lst[pivot] <= lst[right]:
            right -= 1
        if right < left:
            lst[right], lst[pivot] = lst[pivot], lst[right]
        else:
            lst[left], lst[right] = lst[right], lst[left]
    quick_sort(lst, right + 1, end)
    quick_sort(lst, start, right - 1)


if __name__ == '__main__':
    # tmp = [3, 1, 2, 4, 2, 5, 1, 4, 1, 1, 1, 2, 4, 1, 1]
    tmp = [3, 1, 2]
    # tmp = [3, 2, 1, 4]
    # tmp = [1,1,1,1]
    # R L
    # tmp = [1, 2, 3, 4, 5]
    quick_sort(tmp, 0, len(tmp) - 1)
    print(tmp)
