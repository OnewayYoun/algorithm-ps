from collections import deque
from typing import List


class Solution:
    """
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]

    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        answer = []
        dq = deque(intervals)
        start, end = dq.popleft()
        while dq:
            new_start, new_end = dq.popleft()
            if end < new_start:
                answer.append([start, end])
                start = new_start
                end = new_end
            elif start <= new_start <= end:
                if start <= new_end <= end:
                    continue
                end = new_end

        answer.append([start, end])

        return answer

    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = [intervals[0]]

        for interval in intervals[1:]:
            if answer[-1][0] <= interval[0] <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1], interval[1])
            else:
                answer.append(interval)
        return answer


print(Solution().merge1(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
