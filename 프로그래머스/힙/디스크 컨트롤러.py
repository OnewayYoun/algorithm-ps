import heapq


def solution(jobs):
    cur_time = 0
    n = len(jobs)
    cnt = 0
    jobs.sort()
    heap = []
    answer = 0
    start = -1

    while cnt < n:
        for request_time, time_consuming in jobs:
            if start < request_time <= cur_time:
                heapq.heappush(heap, (time_consuming, request_time))
        if len(heap) > 0:
            cur = heapq.heappop(heap)
            start = cur_time
            cur_time += cur[0]
            answer += (cur_time - cur[1])
            cnt += 1
        else:
            cur_time += 1
    return answer // n


print(solution([[0, 3], [1, 9], [3, 5]]))
