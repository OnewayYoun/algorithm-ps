# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    pos_nums = set([num for num in A if num > 0])
    smallest_num = 1
    while smallest_num in pos_nums:
        smallest_num += 1

    return smallest_num


if __name__ == '__main__':
    A = [1, 3, 6, 4, 1, 2]
    print(solution(A))