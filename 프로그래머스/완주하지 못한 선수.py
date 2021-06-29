p = ["mislav", "stanko", "mislav", "ana", "mislav"]
c = ["stanko", "ana", "mislav"]

from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    #print(*[k for k, v  in answer.items()])
    return str(*answer)

print(solution(p, c))