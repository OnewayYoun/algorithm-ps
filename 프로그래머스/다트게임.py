'''
1)	1S2D*3T	    37	    11 * 2 + 22 * 2 + 33
2)	1D2S#10S	9	    12 + 21 * (-1) + 101
3)	1D2S0T	    3	    12 + 21 + 03
4)	1S*2T*3S	23	    11 * 2 * 2 + 23 * 2 + 31
5)	1D#2S*3S	5	    12 * (-1) * 2 + 21 * 2 + 31
6)	1T2D3D#	    -4	    13 + 22 + 32 * (-1)
7)	1D2S3T* 	59	    12 + 21 * 2 + 33 * 2
'''


import re

def solution(dartResult):
    scores = re.findall('[0-9]+[SDT][*#]?', dartResult)
    tmp = []
    for i, v in enumerate(scores):
        num = ''
        power = 0
        option = 1
        for j in v:
            if j.isdigit():
                num += j
            elif j in ['S', 'D', 'T']:
                if j == 'S':
                    power = 1
                elif j == 'D':
                    power = 2
                elif j == 'T':
                    power = 3
            elif j in ['*', '#']:
                if j == '*':
                    option = 2
                elif j == '#':
                    option = -1
        tmp.append((int(num)**power) * option)
        if i != 0 and option == 2:
            tmp[i-1] *= option

    return sum(tmp)


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))


print('\n\n\n')

def solution2(dart):
    power = {
        'S' : 1,
        'D' : 2,
        'T' : 3,
    }
    option = {
        '' : 1,
        '*' : 2,
        '#' : -1,
    }

    answer = re.findall('(\d+)([SDT])([*#]?)', dart)
    for i, v in enumerate(answer):
        answer[i] = int(v[0]) ** power[v[1]] * option[v[2]]
        if i != 0 and v[2] == '*':
            answer[i-1] *= 2
    return sum(answer)


print(solution2("1S2D*3T"))
print(solution2("1D2S#10S"))
print(solution2("1D2S0T"))
print(solution2("1S*2T*3S"))
print(solution2("1D#2S*3S"))
print(solution2("1T2D3D#"))
print(solution2("1D2S3T*"))




#출처: 프로그래머스 코딩테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/17682