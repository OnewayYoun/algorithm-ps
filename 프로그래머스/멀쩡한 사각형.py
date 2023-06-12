from math import gcd

def solution(w,h):
    tmp = gcd(w, h)
    return w * h - (w + h - tmp)