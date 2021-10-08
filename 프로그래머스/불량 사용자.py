from itertools import permutations


def check(per, b):
    for i in range(len(b)):
        if len(per[i]) != len(b[i]):
            return False
        else: #길이가 같을경우
            for j in range(len(b[i])):
                if b[i][j] == '*':
                    continue
                elif per[i][j] == b[i][j]:
                    continue
                elif per[i][j] != b[i][j]:
                    return False
    return True


def solution(u, b):
    answer = []
    pers = list(permutations(u, len(b)))

    for per in pers:
        if check(per, b):
            tmp = set(per)
            if tmp not in answer:
                answer.append(tmp)
    return len(answer)


u = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b = ["*rodo", "*rodo", "******"]

print(solution(u, b))

#출처: 프로그래머스 코딩테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/64064
