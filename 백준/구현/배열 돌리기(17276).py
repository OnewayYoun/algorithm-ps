'''
4
5 45
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
5 -45
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
5 135
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
5 360
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''

import sys
from copy import deepcopy


def rotate(lst: list, degree: int, n: int) -> list:
    copied_lst = deepcopy(lst)
    if degree < 0:
        degree += 360
    degree %= 360
    if degree == 0:
        return copied_lst
    for _ in range(degree//45):
        for i in range(n):
            copied_lst[i][n // 2] = lst[i][i]
            copied_lst[i][n - i - 1] = lst[i][n // 2]
            copied_lst[n // 2][i] = lst[n - i - 1][i]
            copied_lst[i][i] = lst[n//2][i]
        lst = deepcopy(copied_lst)
    return copied_lst


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    answer = []
    for testcase in range(T):
        n, degree = map(int, sys.stdin.readline().split())
        array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
        answer.extend(rotate(array, degree, n))

    for i in answer:
        print(*i)
