from typing import List

'''
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites_map = {i: [] for i in range(numCourses)}
        visited = set()
        for course, prerequisite in prerequisites:
            prerequisites_map[course].append(prerequisite)

        def dfs(course):
            if course in visited:
                return False
            if not prerequisites_map[course]:
                return True

            visited.add(course)
            for pre in prerequisites_map[course]:
                if not dfs(pre):
                    return False
            prerequisites_map[course] = []
            visited.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


print(Solution().canFinish(numCourses=2, prerequisites=[[1, 0]]))
