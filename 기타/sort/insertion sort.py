def insertion_sort(lst: list):
    for i in range(1, len(lst)):
        while i > 0 and lst[i] < lst[i - 1]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1


# def insertion_sort(l):
#     for i in range(1, len(l)):
#         value = l[i]
#         j = i - 1
#         while j >= 0 and value < l[j]:
#             l[j + 1] = l[j]
#             j -= 1
#         l[j + 1] = value


if __name__ == '__main__':
    tmp = [3, 1, 2, 4, 2, 5, 1, 3]
    # tmp = [1, 2, 3, 4, 5]
    insertion_sort(tmp)
    print(tmp)
