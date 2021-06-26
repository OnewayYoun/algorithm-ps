N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
#result = [3,4,2,1,5]

from collections import Counter

def solution(N, stages):
    answer = {}
    total = len(stages)
    count = Counter(stages)
    for i in range(N):
        if total != 0:
            answer[i+1] = count[i+1] / total
            total -= count[i+1]
        else:
            answer[i+1] = 0
    print(answer)

    return [i[0] for i in sorted(answer.items(), key=lambda x: (-x[1], x[0]))] #value로 내림차순 진행후 key로 오름차순


print(solution(N, stages))

#출처: 프로그래머스 코딩테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/42889



'''
return값을 다른식으로 표현 가능:

a = {1: 0.125, 2: 0.42857142857142855, 3: 0.5, 4: 0.5, 5: 0.0}

#a[x]는 각 key에 대응되는 value를 뜻한다.
print(sorted(a, key=lambda x:-a[x]))

'''