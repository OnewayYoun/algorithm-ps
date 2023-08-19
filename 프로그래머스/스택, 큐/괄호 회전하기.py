from collections import deque

parentheses = {'(': ')', '[': ']', '{': '}'}


def solution(s):
    def is_valid(input_str):
        stack = []
        for i in input_str:
            if i in parentheses:
                stack.append(i)
            else:
                if not stack:
                    return False
                if parentheses[stack.pop()] != i:
                    return False
        return True if not stack else False

    dq = deque(s)
    answer = 0
    for _ in range(len(s)):
        dq.rotate(-1)
        if is_valid(''.join(dq)):
            answer += 1
    return answer
