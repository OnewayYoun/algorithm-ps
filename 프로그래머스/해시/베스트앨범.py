from collections import defaultdict
from heapq import heappush, heappop


def solution(genres, plays):
    answer = []
    count_dict = defaultdict(int)
    find_dict = defaultdict(list)
    for i in range(len(genres)):
        count_dict[genres[i]] += plays[i]
        heappush(find_dict[genres[i]], (-plays[i], i))
    for key, val in sorted(count_dict.items(), key=lambda x: x[1], reverse=True):
        for _ in range(2):
            if find_dict[key]:
                answer.append(heappop(find_dict[key])[1])
    return answer


if __name__ == '__main__':
    genres, plays, sol = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500], [4, 1, 3, 0]
    print(solution(genres, plays))
