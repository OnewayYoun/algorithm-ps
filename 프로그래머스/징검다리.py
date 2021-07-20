'''
제거한 바위의 위치	    각 바위 사이의 거리	거리의 최솟값
[21, 17]	        [2, 9, 3, 11]	    2
[2, 21]	            [11, 3, 3, 8]	    3
[2, 11]	            [14, 3, 4, 4]	    3
[11, 21]        	[2, 12, 3, 8]	    2
[2, 14]	            [11, 6, 4, 4]	    4

distance	rocks	                n	    return
25	        [2, 14, 11, 21, 17]	    2	    4
'''


def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)

    L, R = 0, distance

    while L <= R:
        mid = (L+R) // 2
        remove_cnt = 0
        curr = 0

        for rock in rocks:
            dist = rock - curr
            if dist < mid:      # mid값보다 작으면 바위제거 카운트수 +1
                remove_cnt += 1
            else:               # mid값보다 크거나 같으면 curr 포지션을 현재 돌위치로 바꾸기
                curr = rock

        if remove_cnt > n:      # remove_cnt가 n보다 더 크면 R을 작게해서 cnt수를 줄이기
            R = mid - 1
        elif remove_cnt <= n:
            L = mid + 1         # remove_cnt가 n보다 크거나 같으면 L를 크게해서 cnt수를 늘리거나 mid값을 늘리기
            answer = mid

    return answer



print(solution(25, [2, 14, 11, 21, 17], 2))

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43236