import sys

input = sys.stdin.readline

'''
if __name__ == '__main__':
    dp = [0] * 91
    dp[0], dp[1] = 0, 1
    for i in range(2, len(dp)):
        dp[i] = dp[i - 1] + dp[i - 2]
    n = int(input())
    print(dp[n])
'''

'''
def fibonacci(num):
    if dp[num] == -1:
        dp[num] = fibonacci(num - 1) + fibonacci(num - 2)
    return dp[num]


if __name__ == '__main__':
    dp = [-1] * 91
    dp[0], dp[1] = 0, 1
    n = int(input())
    print(fibonacci(n))
'''

'''
def fib(x):
    if d[x] != 0:
        return d[x]
    d[x] = fib(x - 1) + fib(x - 2)
    return d[x]


if __name__ == '__main__':
    d = [0] * 91
    d[1], d[2] = 1, 1
    n = int(input())
    print(fib(n))
'''

'''
def fib(x):
  if x == 1 or x == 2:
    return 1
  if d[x] != 0:
    return d[x]

  d[x] = fib(x-1) + fib(x-2)
  return d[x]

if __name__ == '__main__':
    d = [0]*91
    n = int(input())
    print(fib(n))
'''
