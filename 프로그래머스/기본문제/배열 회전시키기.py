from collections import deque


def solution(numbers, direction):
    dq = deque(numbers)
    if direction == 'right':
        dq.rotate(1)
    else:
        dq.rotate(-1)
    return list(dq)

# def solution(numbers, direction):
#     if direction == 'right':
#         return [numbers[-1]] + numbers[:-1]
#     else:
#         return numbers[1:] + [numbers[0]]
