def selection_sort(lst: list):
    for i in range(len(lst)):
        min_idx = i
        for j in range(1 + i, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]


if __name__ == '__main__':
    tmp = [3, 1, 2, 4, 2, 5, 1, 3]
    # tmp = [1, 2, 3, 4, 5]
    selection_sort(tmp)
    print(tmp)
