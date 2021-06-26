land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
#answer = 16

def solution(land):

    for i in range(0, len(land)-1):
        for j in range(4):
            land[i+1][j] = max(land[i][:j] + land[i][j+1:]) + land[i+1][j]

    return max(land[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))

#출처: 프로그래머스 코딩테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/12913