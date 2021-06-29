p = ["mislav", "stanko", "mislav", "ana"]
c = ["stanko", "ana", "mislav"]

from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    #print(*[k for k, v  in answer.items()])
    return str(*answer)

print(solution(p, c))

#출처: 프로그래머스 코딩테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/42576