'''
numbers     	          return
[6, 10, 2]  	         "6210"
[3, 30, 34, 5, 9]	     "9534330"
'''

def solution(numbers):
    a = sorted(map(str, numbers), key = lambda x: x*3, reverse=True)
    #x*3하는 이유 : 0이상 1000이하 숫자이기떄문에 예를 들어 9와 993을 비교할때 999, 993993993을해서 3자리수까지 비교해서 9가 먼저 나오게 할수있기때문
    print(a)
    return str(int(''.join(a)))

#[0, 0, 0, 0]같은 경우 0000을 int로 변화해서 0으로 만들고 다시 str으로 리턴하기 위해

print(solution([3, 30, 34, 5, 9]))