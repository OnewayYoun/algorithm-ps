import math
from itertools import permutations


def is_prime(number):
    if number in (0, 1):
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if (number % i) == 0:
            return False
    return True


def solution(numbers):
    answer_set = set()
    for i in range(len(numbers)):
        for perm in permutations(numbers, i + 1):
            tmp = int(''.join(perm))
            if is_prime(tmp):
                answer_set.add(tmp)
    return len(answer_set)


if __name__ == '__main__':
    numbers = '17'  # 3
    # numbers = '011'  # 2
    print(solution(numbers))
