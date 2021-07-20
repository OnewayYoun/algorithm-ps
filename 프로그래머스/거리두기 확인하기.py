'''
    places	                                                result
[   ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]   ]	    [1, 0, 1, 1, 1]
'''

from collections import deque

SIZE = 5


def bfs(place, x, y):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False for _ in range(SIZE)] for _ in range(SIZE)]

    # deque에 리스트 넣을떄 조심할것 deque([x, y, 0]) -> deque([x, y, 0])
    # dp = deque(), dp.append([x, y, 0]) -> deque([[x, y, 0]]) 이렇게 되어야 정상
    # Hence, deque([[x, y, 0]])
    dq = deque([[x, y, 0]])
    visited[x][y] = True

    while dq:
        current = dq.popleft()

        if 1 <= current[2] <= 2 and place[current[0]][current[1]] == 'P':
            return False
        if current[2] >= 3:
            return True

        for i in range(4):
            nx = current[0] + dx[i]
            ny = current[1] + dy[i]
            nd = current[2] + 1

            if 0 <= nx < 5 and 0 <= ny < 5:
                if place[nx][ny] != 'X' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dq.append([nx, ny, nd])

    return True


def solution(places):
    answer = []

    for place in places:
        check = True
        for x in range(SIZE):
            for y in range(SIZE):
                if place[x][y] == 'P':
                    if not bfs(place, x, y):
                        check = False
                        break
            if not check:
                break
        if not check:
            answer.append(0)
        else:
            answer.append(1)

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/81302