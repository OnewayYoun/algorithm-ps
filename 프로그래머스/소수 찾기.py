'''
numbers	return
"17"	3
"011"	2
'''
from itertools import permutations

def is_prime(x):
    x = int(x)
    if x < 2:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    for i in range(1, len(numbers)+1):
        tmp = list(map(''.join, permutations(numbers, i)))
        for j in tmp:
            if is_prime(j):
                answer.add(int(j))
    print(answer)
    return len(answer)

print(list(map(''.join, permutations('011', 1))))
print(list(map(''.join, permutations('011', 2))))
print(list(map(''.join, permutations('011', 3))))


print(solution("011"))

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42839