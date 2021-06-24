def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()


print(solution('a234'))
print(solution('1234'))


#출처: 프로그래머스 코딩테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/12918