'''
numbers	            target	    return
[1, 1, 1, 1, 1]	    3	        5
'''

from itertools import product

def solution(numbers, target):
    new_nums = [(i, -i) for i in numbers]
    res = list(map(sum, product(*new_nums)))

    return res.count(target)

def solution1(numbers, target):
    # 더하고 빼기를 재귀로 풀었을때 타겟넘버가 0이고 리스트가 비어있을떄 충족하므로 1을 리턴해서 카운트 늘리기
    if not numbers and target == 0:
        return 1
    # 타겟넘버가 충족안되고 리스트가 비어있으면 0을 리턴해서 카운트 관여X
    elif not numbers:
        return 0
    # 재귀로 하나씩 빼고 더하기
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

print(solution([1, 1, 1, 1, 1], 3))
print(solution1([1, 1, 1, 1, 1], 3))

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43165