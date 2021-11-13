# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import re


def solution(N):
    # write your code in Python 3.6
    bin_num = format(N, 'b')
    print(bin_num)
    l = re.findall('(?<=1)0+?(?=1)', bin_num)
    if l:
        return len(max(l, key=len))
    else:
        return 0


print(solution(1041))
