from collections import deque


def solution(enter, leave):
    answer = [0] * len(enter)
    room = []
    dq = deque(leave)

    for i in enter:
        for j in room:
            answer[j-1] += 1
        answer[i-1] += len(room)
        room.append(i)

        while room and dq[0] in room:
            room.remove(dq.popleft())

    return answer


if __name__ == '__main__':
    enter, leave, result = [1, 3, 2], [1, 2, 3], [0, 1, 1]
    print(solution(enter, leave))

    enter, leave, result = [1, 4, 2, 3], [2, 1, 3, 4], [2, 2, 1, 3]
    print(solution(enter, leave))

    enter, leave, result = [3, 2, 1], [2, 1, 3], [1, 1, 2]
    print(solution(enter, leave))

    enter, leave, result = [3, 2, 1], [1, 3, 2], [2, 2, 2]
    print(solution(enter, leave))

    enter, leave, result = [1, 4, 2, 3], [2, 1, 4, 3], [2, 2, 0, 2]
    print(solution(enter, leave))
