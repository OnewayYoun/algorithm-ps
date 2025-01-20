from typing import List


class Solution:
    """
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    """

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        answer = [intervals[0]]

        for interval in intervals[1:]:
            if answer[-1][0] <= interval[0] <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1], interval[1])
            else:
                answer.append(interval)
        return answer


print(Solution().insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
