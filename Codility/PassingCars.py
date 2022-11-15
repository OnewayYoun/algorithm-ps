# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.8.10
    answer = 0
    pre_zeros = 0

    for i in A:
        if i == 0:
            pre_zeros += 1
        elif i == 1:
            answer += pre_zeros
    return -1 if answer > 1000000000 else answer
