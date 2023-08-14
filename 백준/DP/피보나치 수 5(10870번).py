import sys

input = sys.stdin.readline


def fibonacci(num):
    if num == 0:
        return 0
    if num in (1, 2):
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))
