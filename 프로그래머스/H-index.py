'''
citations	        return
[3, 0, 6, 1, 5]	    3
'''


def solution(citations):
    tmp = sorted(citations, reverse=True)
    cnt = 0
    for i in range(len(tmp)):
        if tmp[i] >= i+1:
            cnt += 1
        else:
            break
    return cnt

def solution1(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

print(solution([3, 0, 6, 1, 5]))
print(solution1([3, 0, 6, 1, 5]))