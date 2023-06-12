import string
from collections import defaultdict


def solution(msg):
    answer = []
    uppercase = string.ascii_uppercase
    dictionary = defaultdict(int)
    num = 1

    for letter in uppercase:
        dictionary[letter] = num
        num += 1
        iterations = 0

    for idx, val in enumerate(msg):
        right = idx
        if iterations != 0:
            iterations -= 1
            continue

        while right < len(msg):
            prev = msg[idx:right + 1]
            if prev not in dictionary:
                answer.append(dictionary[msg[idx:right]])
                dictionary[prev] = num
                num += 1
                break
            right += 1
        if right == len(msg) and prev in dictionary:
            answer.append(dictionary[prev])
            break
        iterations = len(prev) - 2

    return answer


if __name__ == '__main__':
    print(solution('KAKAO'))