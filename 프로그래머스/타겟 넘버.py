'''
numbers	            target	    return
[1, 1, 1, 1, 1]	    3	        5
'''

from itertools import product

def solution(numbers, target):
    new_nums = [(i, -i) for i in numbers]
    res = list(map(sum, product(*new_nums)))

    return  res.count(target)

print(solution([1, 1, 1, 1, 1], 3))