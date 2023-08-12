def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[0])
    start, end = routes[0][0], routes[0][1]
    for i in routes[1:]:
        s, e = i
        if start <= s <= end:
            start = s
            end = min(end, e)
        else:
            answer += 1
            start = s
            end = e
    return answer


if __name__ == '__main__':
    routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]  # 2
    print(solution(routes))
