def solution(sequence, k):
    answer = []
    left, total = 0, 0
    length = float('inf')

    for right, val in enumerate(sequence):
        total += val
        if total > k:
            while total > k and left < right:
                total -= sequence[left]
                left += 1
        if total == k:
            tmp = right - left
            if tmp < length:
                length = tmp
                answer = [left, right]

    return answer


solution([1, 1, 1, 2, 3, 4, 5], 5)
