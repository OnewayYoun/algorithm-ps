#방금그곡
import datetime
import math
import re

def replace_sharp(string):
    if 'C#' in string:
        string = string.replace('C#', 'c')
    if 'D#' in string:
        string = string.replace('D#', 'd')
    if 'F#' in string:
        string = string.replace('F#', 'f')
    if 'G#' in string:
        string = string.replace('G#', 'g')
    if 'A#' in string:
        string = string.replace('A#', 'a')

    return string


def time_diff(info):
    t = int((datetime.datetime.strptime(info[1], '%H:%M') - datetime.datetime.strptime(info[0], '%H:%M')).seconds / 60)

    return t


def repeat_to_length(string, length):
    return (string * math.ceil(length / len(string)))[:length]


def solution(m, musicinfos):
    m = replace_sharp(m)

    infos = [i.split(',') for i in musicinfos]
    infos = [(time_diff(i), i[2], repeat_to_length(replace_sharp(i[3]), time_diff(i))) for i in infos]
    infos = [(i[0], i[1], len(re.findall(m + '(?![#])', i[2]))) for i in infos]
    final_answer = [(i[0], i[1]) for i in infos if i[2] != 0]

    if final_answer:
        return max(final_answer, key=lambda x: x[0])[1]
    else:
        return '(None)'

m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))

'''
b = '12:30'
a = '14:20'

a = datetime.datetime.strptime(a, '%H:%M') - datetime.datetime.strptime(b, '%H:%M')
print(a.seconds/60)
print(a.total_seconds()/60)
'''

#출처: 프로그래머스 코딩테스트 연습, https://programmers.co.kr/learn/courses/30/lessons/17683