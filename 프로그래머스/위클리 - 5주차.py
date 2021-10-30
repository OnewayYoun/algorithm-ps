from itertools import product

def solution(word):
    answer = []
    words = ['A', 'E', 'I', 'O', 'U']

    for i in range(6):
        for j in product(words, repeat=i):
            answer.append(''.join(j))

    answer.sort()

    return answer.index(word)


if __name__ == '__main__':
    word = "AAAAE"
    result = 6
    print(solution(word))

    word = "AAAE"
    result = 10
    print(solution(word))

    word = "I"
    result = 1563
    print(solution(word))

    word = "EIO"
    result = 1189
    print(solution(word))
