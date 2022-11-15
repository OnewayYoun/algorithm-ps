A = [3, 4, 3, 2, 3, -1, 3, 3]

from collections import Counter
def solution(A):
    # write your code in Python 3.6
    length = len(A)//2
    cnt = Counter(A)
    dominator = [i[0] for i in cnt.items() if i[1] > length]
    answer = []
    for i, v in enumerate(A):
        if v in dominator:
            answer.append(i)
    if not answer:
        return -1
    else:
        return answer[0]

print(solution(A))

def solution1(A):
    # write your code in Python 3.6
    dominator = None
    length = len(A) // 2
    cnt = Counter(A)
    for x in cnt.items():
        if x[1] > length:
            dominator = x[0]
            break
    if dominator == None:
        return -1
    else:
        return A.index(dominator)


print(solution1(A))

#출처 : https://app.codility.com/programmers/lessons/8-leader/dominator/
