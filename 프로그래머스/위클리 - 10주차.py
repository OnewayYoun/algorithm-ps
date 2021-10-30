from itertools import combinations


def intersection_of_lines(eq1, eq2):
    try:
        x = (eq1[1] * eq2[2] - eq1[2] * eq2[1]) / (eq1[0] * eq2[1] - eq1[1] * eq2[0])
        y = (eq1[2] * eq2[0] - eq1[0] * eq2[2]) / (eq1[0] * eq2[1] - eq1[1] * eq2[0])
        if x.is_integer() and y.is_integer():
            return (int(x), int(y))
        else:
            pass
    except ZeroDivisionError:
        pass


def solution(line):
    answer = []
    for i in combinations(line, 2):
        tmp = intersection_of_lines(i[0], i[1])
        if tmp:
            answer.append(tmp)
    max_width, min_width = max(answer, key=lambda x: x[0])[0], min(answer, key=lambda x: x[0])[0]
    max_height, min_height = max(answer, key=lambda x: x[1])[1], min(answer, key=lambda x: x[1])[1]

    final_answer = []
    for i in range(max_height, min_height - 1, -1):
        tmp = ''
        for j in range(min_width, max_width + 1):
            if (j, i) in answer:
                tmp += '*'
            else:
                tmp += '.'
        final_answer.append(tmp)

    return final_answer


if __name__ == '__main__':
    line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
    result = ["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........",
              "*.......*"]
    print(solution(line))

    line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
    result = ["*.*"]
    print(solution(line))

    line = [[1, -1, 0], [2, -1, 0]]
    result = ["*"]
    print(solution(line))

    line = [[1, -1, 0], [2, -1, 0], [4, -1, 0]]
    result = ["*"]
    print(solution(line))
