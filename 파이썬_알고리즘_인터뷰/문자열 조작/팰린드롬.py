from collections import deque
import re


def solution_with_list(string: str) -> bool:
    strs = [char for char in string if char.isalnum()]
    while len(strs) > 1:
        if strs.pop(0) != strs.pop(-1):
            return False
    return True


def solution_with_deque(string: str) -> bool:
    dq = deque([char for char in string if char.isalnum()])
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


def solution_with_slicing(string: str) -> bool:
    string = string.lower()
    string = re.sub('[^a-z0-9]', '', string)
    return string == string[::-1]


if __name__ == '__main__':
    print(solution_with_list("a:1:a"))
    print(solution_with_deque("a:1:a"))
    print(solution_with_slicing("a:1:a"))
