def solution(answers):
    counts = [0, 0, 0]
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for idx, val in enumerate(answers):
        if val == first[idx % 5]:
            counts[0] += 1
        if val == second[idx % 8]:
            counts[1] += 1
        if val == third[idx % 10]:
            counts[2] += 1
    max_count = max(counts)
    return [i + 1 for i in range(3) if max_count == counts[i]]


if __name__ == '__main__':
    answers = [1, 2, 3, 4, 5]  # 1
    # answers = [1, 3, 2, 4, 2]  # [1,2,3]
    print(solution(answers))
