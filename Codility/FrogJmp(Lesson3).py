'''
X = 10
Y = 85
D = 30
X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.
'''


def solution(X, Y, D):
    if (Y-X)%D == 0:
        return (Y-X)//D
    else:
        return (Y-X)//D + 1


print(solution(10, 85, 30))


#출처 : https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
