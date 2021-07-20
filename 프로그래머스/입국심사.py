'''
n	    times	    return
6	    [7, 10]	    28
'''

def solution(n, times):
    answer = 0
    L = 0
    R = max(times)*n

    while(L<=R):
        mid = (L+R) // 2
        total = 0
        for time in times:
            total += mid//time
        if total >= n:
            answer = mid
            R = mid-1
        else:
            L = mid+1

    return answer



print(solution(6, [7, 10]))

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43238