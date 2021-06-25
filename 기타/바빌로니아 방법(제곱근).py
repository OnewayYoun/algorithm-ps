def sqrt(x):
    n = 1
    #루프를 더 많이 돌릴수록 정확해짐
    for i in range(10):
      n = (n+(x/n))/2
    return print('{}의 제곱근 = {}'.format(x,n))


sqrt(144)
