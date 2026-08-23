from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        answer = []
        for person in people:
            answer.insert(person[1] , person)
        return answer


print(Solution().reconstructQueue(people=[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
# Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]