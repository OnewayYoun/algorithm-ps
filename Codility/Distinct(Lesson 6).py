A = [1, 1, 3, 3, 2, 1, 3]


def solution1(A):
    return len(set(A))


from collections import Counter


def solution2(A):
    return len(Counter(A))


print(solution1(A))

print(solution2(A))

#출처 : https://app.codility.com/programmers/lessons/6-sorting/distinct/