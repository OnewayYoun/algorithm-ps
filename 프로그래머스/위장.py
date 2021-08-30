from collections import defaultdict


def solution(clothes):
    answer = 1
    d = defaultdict(int)

    for i in clothes:
        d[i[1]] += 1

    for i in d.values():
        answer *= (i + 1)

    return answer - 1

# 출처: https://programmers.co.kr/learn/courses/30/lessons/42578