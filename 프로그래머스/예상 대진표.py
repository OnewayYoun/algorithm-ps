def solution(n,a,b):
    answer = 0

    while a != b:
        answer += 1
        a = (a+1) // 2
        b = (b+1) // 2

    return answer

print(solution(8, 4, 7))

#출처: 프로그래머스 코딩테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/12985


'''
비트로 푸는 방식
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()
'''