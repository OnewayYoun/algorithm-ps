def bubble_sort(lst: list):
    for i in range(len(lst) - 1):
        flag = True
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                flag = False
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if flag:
            break


if __name__ == '__main__':
    tmp = [3, 1, 2, 4, 2, 5, 1, 3]
    # tmp = [1, 2, 3, 4, 5]
    bubble_sort(tmp)
    print(tmp)
