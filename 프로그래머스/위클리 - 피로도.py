from itertools import permutations


def solution(k, dungeons):
    possible = []
    for per in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0
        for i in per:
            if tmp >= i[0]:
                tmp -= i[1]
                cnt += 1
        possible.append(cnt)

    return max(possible)


# 백트래킹 다른사람 풀이
# answer = 0
# N = 0
# visited = []
#
#
# def dfs(k, cnt, dungeons):
#     global answer
#     if cnt > answer:
#         answer = cnt
#
#     for j in range(N):
#         if k >= dungeons[j][0] and not visited[j]:
#             visited[j] = 1
#             dfs(k - dungeons[j][1], cnt + 1, dungeons)
#             visited[j] = 0
#
#
# def solution(k, dungeons):
#     global N, visited
#     N = len(dungeons)
#     visited = [0] * N
#     dfs(k, 0, dungeons)
#     return answer


if __name__ == '__main__':
    k, dungeons, result = 80, [[80, 20], [50, 40], [30, 10]], 3
    print(solution(k, dungeons))
