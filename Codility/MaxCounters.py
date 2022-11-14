# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.8.10
    max_counter = 0
    answer = [0] * N
    cache = 0

    for val in A:
        if val > N:
            cache = max_counter
        else:
            if answer[val-1] < cache:
                answer[val-1] = 1 + cache
            else:
                answer[val-1] += 1
            max_counter = answer[val-1] if answer[val-1] > max_counter else max_counter
    for i in range(N):
        if answer[i] < cache:
            answer[i] = cache
    return answer
