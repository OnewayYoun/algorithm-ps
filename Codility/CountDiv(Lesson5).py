'''
A~B 까지 있는 숫자들둥 K롤 나누어 떨어지는 갯수 구하기
A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B
'''


def solution(A, B, K):
    if A%K == 0:
        return B//K - A//K + 1
    else:
        return B//K - A//K


print(solution(6, 11, 2))


#출처 : https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
