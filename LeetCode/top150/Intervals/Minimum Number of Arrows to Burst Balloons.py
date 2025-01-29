from typing import List


class Solution:
    """
    Input: points = [[10,16],[2,8],[1,6],[7,12]]
    Output: 2
    Explanation: The balloons can be burst by 2 arrows:
    - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
    - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

    Input: points = [[1,2],[3,4],[5,6],[7,8]]
    Output: 4

    Input: points = [[1,2],[2,3],[3,4],[4,5]]
    Output: 2
    """

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        answer = 1
        cur = points[0][1]

        for interval in points[1:]:
            if interval[0] <= cur <= interval[1]:
                continue
            else:
                cur = interval[1]
                answer += 1

        return answer


print(Solution().findMinArrowShots([[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]))
