'''
arr1	                            arr2	                            return
[[1, 4], [3, 2], [4, 1]]	        [[3, 3], [3, 3]]	                [[15, 15], [15, 15], [15, 15]]
[[2, 3, 2], [4, 2, 4], [3, 1, 4]]	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	[[22, 22, 11], [36, 28, 18], [29, 20, 14]]
'''
a = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
b = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr2[0])):
            sum = 0
            for k in range(len(arr1[0])):
                sum += arr1[i][k] * arr2[k][j]
            answer[i].append(sum)

    return answer


def solution1(arr1, arr2):
    return [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*arr2)] for A_row in arr1]

print(solution1(a, b))



