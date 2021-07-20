'''
s	                result
"one4seveneight"	1478
"23four5six7"	    234567
"2three45sixseven"	234567
"123"	            123

0	zero
1	one
2	two
3	three
4	four
5	five
6	six
7	seven
8	eight
9	nine
'''

# 0.03ms
def solution(s):
    return int(s.lower().replace('zero', '0').replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9'))


# 0.03ms
num_dict = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def solution1(s):
    s = s.lower()
    for k, v in num_dict.items():
        s = s.replace(k, v)
    return int(s)


print(solution("2three45Sixseven"))
print(solution1("2three45Sixseven"))


# 출처 : https://programmers.co.kr/learn/courses/30/lessons/81301