from collections import defaultdict


def solution(n, lost, reserve):
    lost, reserve = set(lost), set(reserve)
    answer = n - len(lost - reserve)
    search_table = defaultdict(bool, {i: True for i in lost - reserve})
    for i in reserve - lost:
        for j in [-1, +1]:
            if search_table[i + j]:
                search_table[i + j] = False
                answer += 1
                break
    return answer


if __name__ == '__main__':
    print(solution(2, [2], [2]))
    print(solution(4, [1, 3], [2, 4]))
