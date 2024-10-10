def factorial_iterative(n):
    res = 1
    for i in range(n, 0, -1):
        res *= i
    return res


def factorial_recursive(n):
    if n <= 1:
        return 1
    res = n * factorial_recursive(n - 1)
    return res


print(factorial_recursive(0))

# def recursive(i):
#     if i == 3:
#         return 'hi'
#     print(f'{i} 번째 재귀함수에서, {i+1}번째 재귀 함수를 호출함')
#     res = recursive(i + 1)
#     print(f'{i} 번째 재귀함수를 종료함')
#     print(res)
#     return i
#
#
# print(recursive(1))
