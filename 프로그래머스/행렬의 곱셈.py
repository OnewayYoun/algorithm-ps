'''
arr1	                            arr2	                            return
[[1, 4], [3, 2], [4, 1]]	        [[3, 3], [3, 3]]	                [[15, 15], [15, 15], [15, 15]]
[[2, 3, 2], [4, 2, 4], [3, 1, 4]]	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	[[22, 22, 11], [36, 28, 18], [29, 20, 14]]
'''

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


a = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
b = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]
print(solution(a, b))

