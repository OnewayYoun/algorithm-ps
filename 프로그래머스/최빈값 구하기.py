from collections import Counter


def solution1(array):
    cnt = Counter(array).most_common()

    if len(cnt) == 1:
        return cnt[0][0]
    else:
        if cnt[0][1] == cnt[1][1]:
            return -1
        else:
            return cnt[0][0]


def solution2(array):
    while len(array) != 0:
        for i, v in enumerate(set(array)):
            array.remove(v)
        if i == 0:
            return v
    return -1


if __name__ == '__main__':
    print(solution1([1, 1, 1, 2, 2, 2, 2]))
    print(solution1([1, 1, 1, 2, 2, 2]))

    print(solution2([1, 1, 1, 2, 2, 2, 2]))
    print(solution2([1, 1, 1, 2, 2, 2]))