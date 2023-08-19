mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 뒤집기
'''
1 2 3    1 4 7
4 5 6 -> 2 5 8     
7 8 9    3 6 9     
'''
new_list = list(map(list, zip(*mylist)))
print(new_list)


# 시계방향 90도 회전
'''
1 2 3    7 4 1
4 5 6 -> 8 5 2
7 8 9    9 6 3
'''
new_list = list(map(list, zip(*mylist[::-1])))
print(new_list)


# 반시계방향 90도 회전
'''
1 2 3    3 6 9
4 5 6 -> 2 5 8
7 8 9    1 4 7
'''
new_list = list(map(list, zip(*mylist)))[::-1]
print(new_list)
