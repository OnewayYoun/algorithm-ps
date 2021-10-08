import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, X = map(int, input().split())
    visitants = list(map(int, input().split()))

    answer = []
    left = 0
    # max_sum = -float('inf')
    sum = 0

    for right in range(N):
        sum += visitants[right]
        if right - left + 1 == X:
            answer.append(sum)
            sum -= visitants[left]
            left += 1

    max_sum = max(answer)
    if max_sum != 0:
        print(max_sum)
        print(answer.count(max_sum))
    else:
        print('SAD')

"""
5 2
1 4 2 5 1

7
1
"""