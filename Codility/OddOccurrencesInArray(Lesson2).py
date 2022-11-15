A = [9, 3, 9, 3, 9, 7, 9]

from collections import Counter

def solution(A):
    A = Counter(A)
    answer = None
    for k, v in A.items():
        if v%2 != 0:
            answer = k
            break

    return answer

print(solution(A))


#출처 : https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
