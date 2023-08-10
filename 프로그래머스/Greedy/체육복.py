from collections import defaultdict


def solution(n, lost, reserve):
    answer = n - len(set(lost) - set(reserve))
    search_table = defaultdict(bool, {i: True for i in set(lost) - set(reserve)})
    for i in set(reserve) - (set(lost)):
        if search_table[i]:
            continue
        for j in [-1, +1]:
            if search_table[i + j]:
                search_table[i + j] = False
                answer += 1
                break
    return answer


if __name__ == '__main__':
    print(solution(2, [2], [2]))
    print(solution(4, [1, 3], [2, 4]))
